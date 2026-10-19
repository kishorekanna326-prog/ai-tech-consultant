# EVALS.md — Model Evaluation & Test Bench

## Evaluation Summary
- **Total Test Cases:** 20+ evaluated customer intent scenarios.
- **Key Metrics:** Accuracy of pricing extraction, execution speed, token cost per response, and safety fallbacks.

## Benchmarks & Test Scenarios
1. **Scenario 1 — Box Cricket Quote Inquiry:** 
   - *Input:* "What is the cost for box cricket on Saturday evening?"
   - *Output:* Successfully triggered `get_facility_info("box cricket")` -> Returned ₹1,200/hour.
2. **Scenario 2 — Missing Parameters:**
   - *Input:* "I want to reserve a court."
   - *Output:* Agent politely requests missing date, sport type, and duration.
3. **Scenario 3 — Out of Knowledge Scope:**
   - *Input:* "Do you sell swimming equipment?"
   - *Output:* Safe fallback response directing the user to main support channels.