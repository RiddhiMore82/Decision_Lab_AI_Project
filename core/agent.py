from core.gemini import ask_gemini


def run_agent(role, responsibility, user_decision, planner_data, user_context):

    prompt = f"""
You are the {role} on the AI Decision Board.

Responsibility:
{responsibility}

----------------------------------------
PLANNER REPORT
----------------------------------------

Category: {planner_data["decision_category"]}

Risk: {planner_data["risk_level"]}

Objective: {planner_data["objective"]}

----------------------------------------
USER DECISION
----------------------------------------

{user_decision}

----------------------------------------
USER INFORMATION
----------------------------------------

{user_context}

The user's answers are complete.

Do NOT ask for more information.
Do NOT mention missing information.

Respond in EXACTLY this format:

### Verdict
(One sentence)

### Key Points
- Bullet 1
- Bullet 2
- Bullet 3

### Recommendation
Maximum 2 sentences.

Rules:

• Maximum 100 words.
• No introductions.
• No long paragraphs.
• No repeated information.
• Be practical and direct.
"""

    return ask_gemini(prompt)