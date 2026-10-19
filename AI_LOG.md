# AI_LOG.md — AI Assistance & Prompt Engineering Log

## Top Prompts Used During Development
1. "How do I configure automatic function calling using `google-genai` SDK in Python?"
2. "Convert `client.models.generate_content` to `client.chats.create` to fix AFC recommendations."
3. "Draft system instructions enforcing a polite support persona for Olympia Sports Zone."
4. "Fix PowerShell environment variable syntax error `$env:GEMINI_API_KEY`."
5. "Structure a multi-tool lookup for sports court pricing and availability."

## Instance of AI Suggestion Rejection
- **AI Suggestion:** Hardcoding raw secret keys inside Python scripts for quick testing.
- **Reason for Rejection:** Violated security practices. Refactored code to securely use `.env` files and environment variable loading.
-