import json

from core.gemini import ask_gemini

PLANNER_PROMPT = """
You are the Planner Agent of Decision Lab.

Your job is to analyze the user's decision and determine:

1. Decision category
2. Risk level
3. Which experts should participate
4. What additional information is needed
5. The user's overall objective

Return ONLY valid JSON.

Use EXACTLY this format:

{
  "decision_category": "",
  "risk_level": "",
  "experts": [],
  "missing_information": [],
  "objective": ""
}

Rules:

- Return ONLY JSON.
- No markdown.
- No code block.
- No explanation.
- Return at most 6 clarification questions.
- Questions should be simple and answerable in under 2 minutes.

decision_category must be one of:

Career
Business
Finance
Education
Personal
Health
Investment
Other

risk_level must be one of:

Low
Medium
High

experts may contain only these IDs:

financial
career
risk
lifestyle
business
education
health
devil
"""


def planner_agent(user_input):

    prompt = f"""
{PLANNER_PROMPT}

User Decision:

{user_input}
"""

    response = ask_gemini(prompt)

    print("\n========== RAW GEMINI RESPONSE ==========")
    print(response)
    print("=========================================\n")

    try:

        data = json.loads(response)

        # Validate required keys
        required_keys = [
            "decision_category",
            "risk_level",
            "experts",
            "missing_information",
            "objective",
        ]

        for key in required_keys:
            if key not in data:
                raise ValueError(f"Missing key: {key}")

        return data

    except json.JSONDecodeError as e:

        print("❌ Planner JSON Decode Error")
        print(e)

        raise RuntimeError(
            "Planner Agent returned invalid JSON.\n\n"
            f"Gemini Response:\n{response}"
        )

    except Exception as e:

        print("❌ Planner Validation Error")
        print(e)

        raise