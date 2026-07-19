import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.types import Completion, CompletionChoice, CompletionUsage

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

if api_key is None:
    raise RuntimeError("API_KEY environment variable not found.")

client.chat.completions.create(model, messages):


def main():
    print("Hello from practice-agent!")



if __name__ == "__main__":
    main()
