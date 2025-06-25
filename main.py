import os
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types


def main():
    if len(sys.argv) <= 1:
        print("Please provide a prompt")
        sys.exit(1)
    user_prompt=sys.argv[1]


    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    if len(sys.argv) > 2 and sys.argv[-1] == "--verbose":
            print("User prompt:", user_prompt)
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)
            print("Response:")
            print(response.text)
    else:   
        print("Response:")
        print(response.text)


if __name__ == "__main__":
    main()