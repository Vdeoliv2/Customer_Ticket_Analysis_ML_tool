import json
import ollama


def create_prompt(ticket_description):
    """
    Create the structured customer-support analysis prompt.
    """

    prompt = f"""
Analyze the following customer-support ticket.

Ticket description:
{ticket_description}

Classify the ticket using exactly one of these categories:
- Technical Issue
- Refund Request
- Cancellation Request
- Billing Inquiry
- Product Inquiry

Return the analysis as JSON using exactly these four fields:

{{
    "Summary": "A short description of the customer's problem",
    "Category": "One of the five allowed ticket categories",
    "Sentiment": "The customer's expressed sentiment",
    "Urgency": "The estimated urgency of the problem"
}}

Return only the JSON object and no additional text.
"""

    return prompt


def analyze_ticket(ticket_description):
    """
    Analyze one ticket using Llama 3.1 through Ollama.

    Returns a Python dictionary.
    """

    if ticket_description.strip() == "":
        return None

    prompt = create_prompt(
        ticket_description
    )

    response = ollama.chat(
        model="llama3.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    response_text = (
        response["message"]["content"]
    )

    analysis = json.loads(
        response_text
    )

    return analysis