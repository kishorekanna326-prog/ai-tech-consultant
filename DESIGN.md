1. Problem Statement
Service businesses lose client deals due to delayed email responses, inaccurate manual pricing quotes, and unstructured scope agreements. This project automates client inquiries and meeting workflows by anchoring agent behavior to a unified Knowledge Base.

2. Component Architecture
- **Task 1 (Knowledge Brain):** Stores product details, pricing, policies, and schedules. Exposed via tool calling.
- **Task 2 (Inbox Agent):** Parses customer emails, queries Task 1 via function calling (`get_facility_info`), and drafts accurate client responses.
- **Task 3 (Meeting to Scope):** Converts raw transcripts into itemized developer tasks and client proposals.

3. Model & Framework Selection
- **Primary Model:** `gemini-3.8-flash` selected for fast inference (<2s execution latency), strong tool-calling reliability, and low cost per 1M tokens.
- **SDK:** Official `google-genai` SDK using `client.chats.create` for native Automatic Function Calling (AFC).