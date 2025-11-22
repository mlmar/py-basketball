import json
from google.genai import types
from lib.ai.client import get_client

def test_gemini(data):
    client = get_client()

    # Specify the model you want to use, e.g., "gemini-2.5-flash".
    model_name = "gemini-2.5-flash"

    prompt = "Who are the most underrated NBA players based on this data set?"
    response = client.models.generate_content(
        model=model_name,
        contents=[
            json.dumps(data),
            prompt
        ]
    )
    print(response.text)