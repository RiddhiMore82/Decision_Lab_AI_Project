import os
import re
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env")

# Create Gemini client
client = genai.Client(api_key=api_key)


def ask_gemini(prompt: str) -> str:
    """
    Sends a prompt to Gemini and returns the response text.

    Raises:
        RuntimeError if Gemini API fails.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if not response.text:
            raise RuntimeError("Gemini returned an empty response.")

        text = response.text.strip()

        # Remove markdown code fences if present
        text = re.sub(r"^```json\s*", "", text)
        text = re.sub(r"^```\s*", "", text)
        text = re.sub(r"\s*```$", "", text)

        return text.strip()

    except Exception as e:
        raise RuntimeError(f"Gemini API Error:\n{e}")