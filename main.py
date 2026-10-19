import os
import httpx
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

app = FastAPI(title="AI Tech Consultant - Knowledge Brain")

# Initialize Gemini Client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

KNOWLEDGE_STORE = []

class QueryRequest(BaseModel):
    question: str

@app.post("/api/ingest")
async def ingest_sitemap():
    global KNOWLEDGE_STORE
    KNOWLEDGE_STORE = []
    
    sitemap_url = "https://mhelp.next3off.com/sitemap.xml"
    
    async with httpx.AsyncClient() as http_client:
        try:
            res = await http_client.get(sitemap_url)
            if res.status_code != 200:
                raise HTTPException(status_code=500, detail="Failed to fetch sitemap")
            
            soup = BeautifulSoup(res.text, 'html.parser')
            urls = [loc.text for loc in soup.find_all('loc')]
            
            count = 0
            for url in urls[:10]:
                page_res = await http_client.get(url)
                if page_res.status_code == 200:
                    page_soup = BeautifulSoup(page_res.text, 'html.parser')
                    text = page_soup.get_text(separator=' ', strip=True)
                    KNOWLEDGE_STORE.append({"url": url, "content": text})
                    count += 1
            
            return {"status": "success", "articles_ingested": count}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/query")
async def query_brain(request: QueryRequest):
    if not KNOWLEDGE_STORE:
        raise HTTPException(status_code=400, detail="Knowledge base is empty. Run /api/ingest first.")
    
    context = "\n\n".join([f"Source: {item['url']}\nContent: {item['content'][:1500]}" for item in KNOWLEDGE_STORE[:5]])
    
    prompt = f"""You are an AI Tech Consultant. Answer the customer question using ONLY the provided knowledge base articles below.
Include source URLs in your answer.

Knowledge Base:
{context}

Question: {request.question}
"""
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return {
            "answer": response.text,
            "sources": [item['url'] for item in KNOWLEDGE_STORE[:5]]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        