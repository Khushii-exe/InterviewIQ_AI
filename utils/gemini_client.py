import json
from google import genai
from config import GEMINI_API_KEY, MODEL_NAME
from utils.prompt_loader import load_all_prompts

client = genai.Client(api_key=GEMINI_API_KEY)

prompts = load_all_prompts()

def build_prompt(interview_json):

    prompt = f"""
{prompts["system"]}

======================================================

{prompts["rubric"]}

======================================================

{prompts["examples"]}

======================================================

OUTPUT SCHEMA

{prompts["schema"]}

======================================================

INTERVIEW DATA

{json.dumps(interview_json, indent=4)}

======================================================

Instructions

Return ONLY valid JSON.

Do NOT wrap JSON inside markdown.

Do NOT explain your reasoning.

Return exactly one JSON object.
"""

    return prompt

def evaluate_with_gemini(interview_json):

    prompt = build_prompt(interview_json)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text