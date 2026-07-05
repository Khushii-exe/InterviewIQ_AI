import json
import re

def parse_gemini_response(response: str):
    # Remove markdown code fences if present
    response = response.strip()
    response = re.sub(r"^```json", "", response)
    response = re.sub(r"^```", "", response)
    response = re.sub(r"```$", "", response)
    response = response.strip()
    try:
        return json.loads(response)

    except json.JSONDecodeError as e:

        raise Exception(
            f"Invalid JSON returned by Gemini.\n{e}\n\n{response}"
        )