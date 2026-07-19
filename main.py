import argparse, os
from posix import confstr_names

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

if api_key is None:
    raise RuntimeError("API_KEY environment variable not found.")


def main():
    parser = argparse.ArgumentParser(
        prog="practice_agent",
        description = "Reinforcing python while experimenting with basic chatbots")
    parser.add_argument("user_prompt", type = str, help = "Chatbot Prompt")
    args = parser.parse_args()

    response = client.chat.completions.create(
        model = "openrouter/free",
        messages=[
            {
                "role": "user",
                "content": args.user_prompt,
            }
        ])
    # Untested v
    if response.usage is None:
        raise RuntimeError("It looks like there may be a failed API request, no tokens were used.")
    # Untested ^
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print(f"Response: {response.choices[0].message.content}")

if __name__ == "__main__":
    main()
