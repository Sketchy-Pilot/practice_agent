import argparse, os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY environment variable not found.")


def main():
    parser = argparse.ArgumentParser(
        prog="practice_agent",
        description = "Reinforcing python while experimenting with basic chatbots")
    parser.add_argument("user_prompt", type = str, help = "Chatbot Prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages:list[ChatCompletionMessageParam]=[
        {"role": "user","content": args.user_prompt},
    ]

    response = client.chat.completions.create(
        model = "openrouter/free",
        messages=messages,
    )
    # Untested v
    if response.usage is None:
        raise RuntimeError("It looks like there may be a failed API request, no tokens were used.")
    # Untested ^
    if args.verbose is True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    print(f"Response: \n{response.choices[0].message.content}")

if __name__ == "__main__":
    main()
