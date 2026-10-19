import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key="AQ.Ab8RN6JVPpm750d7LofDZ08Vl-s-rJwnvYfQ2uywUt3I_5QL3w")

# --- KNOWLEDGE BASE / TOOL DEFINITIONS ---
def get_facility_info(sport_name: str) -> str:
    """
    Returns pricing, timings, and availability information for sports at Olympia Sports Zone.
    Args:
        sport_name: The name of the sport requested (e.g., box cricket, football, tennis, pickleball).
    """
    sport = sport_name.lower()
    
    knowledge_base = {
        "box cricket": "Box Cricket is ₹1,200/hour. Slots available daily from 6 AM to 11 PM. Night lights included.",
        "football": "5-a-side Football turf is ₹1,500/hour. Open 6 AM to 11 PM.",
        "pickleball": "Pickleball court is ₹800/hour. Equipment included upon request.",
        "tennis": "Tennis court is ₹1,000/hour. Coaching slots are available in the mornings (6 AM - 9 AM)."
    }
    
    for key in knowledge_base:
        if key in sport:
            return knowledge_base[key]
            
    return "We offer Box Cricket, Football, Tennis, Pickleball, Volleyball, and Basketball. Please contact support for specific pricing."

# --- MAIN AGENT FUNCTION ---
def run_inbox_agent():
    print("Processing incoming email...")
    
    # Sample customer inquiry email
    incoming_email = """
    Subject: Court Booking Inquiry
    Hi, 
    I'd like to ask about booking a box cricket court for this Saturday at 6 PM. 
    Can you tell me the price per hour and if equipment is provided?
    
    Thanks,
    Rahul
    """
    
    prompt = f"Analyze and draft a friendly, professional response to this client email:\n\n{incoming_email}"
    
    # Configure System Instructions and Tools
    config = types.GenerateContentConfig(
        system_instruction=(
            "You are an AI Email Assistant for 'Olympia Sports Zone'. "
            "Your job is to answer customer emails politely and accurately. "
            "Always use the available tools to lookup pricing or facility details before answering."
        ),
        tools=[get_facility_info],  # Automatic function calling enabled
        temperature=0.3
    )
    
    try:
        # Use client.chats.create for automatic function calling (recommended by SDK)
        chat = client.chats.create(
            model='gemini-3.8-flash',
            config=config
        )
        
        response = chat.send_message(prompt)
        
        print("\n--- GENERATED EMAIL DRAFT ---")
        print(response.text)
        
    except Exception as e:
        print(f"Agent error: {str(e)}")

if __name__ == "__main__":
    run_inbox_agent()