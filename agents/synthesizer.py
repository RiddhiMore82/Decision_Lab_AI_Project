from core.gemini import ask_gemini


def synthesizer_agent(decision, planner, reports):

    prompt = f"""
You are the Chairperson of the AI Decision Board.

Decision:
{decision}

Planner:
{planner}

Expert Reports:
{reports}

Your job is NOT to repeat every expert.

Instead:

• Combine their opinions.
• Resolve disagreements.
• Produce one clear recommendation.

Return ONLY this format:

# 🏛 Board Verdict

## Recommendation
Proceed / Wait / Avoid

## Confidence
0-100%

## Why?
Maximum 4 bullet points.

## Biggest Risks
Maximum 3 bullet points.

## Next Steps
1.
2.
3.

Maximum 180 words.

Be concise.
"""
    return ask_gemini(prompt)