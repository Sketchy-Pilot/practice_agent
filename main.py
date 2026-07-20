import argparse
from difflib import context_diff
from operator import call
import os
import json
from prompts import system_prompt
from call_function import available_functions, call_function

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
        {"role": "system", "content": system_prompt},
        {"role": "user","content": args.user_prompt},
    ]
    for _ in range(20):
        response = client.chat.completions.create(
            model = "openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        if response.usage is None:
            raise RuntimeError("It looks like there may be a failed API request, no tokens were used.")

        if args.verbose is True:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")



        message = response.choices[0].message
        messages.append(message)


        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, verbose= args.verbose)
                messages.append(result_message)
                if not result_message["content"]:
                    raise Exception("Content is empty")
                if args.verbose:
                    print(f"-> {result_message['content']}")

        else:
            print(message.content)
            return

if __name__ == "__main__":
    main()
