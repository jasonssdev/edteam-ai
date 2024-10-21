from openai import OpenAI
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()
OAI_API_KEY = os.getenv("openai_api_edt")
OAI_ORGANIZATION = os.getenv("openai_organization")
OAI_PROJECT = os.getenv("openai_project")

client = OpenAI(api_key=OAI_API_KEY, organization=OAI_ORGANIZATION, project=OAI_PROJECT)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "system",
        "content": "You are a expert in electronic music",
    }, {
        "role": "user",
        "content": "Who was the best dj during 2023?"
    }],
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={"type": "text"},
)

print(response.choices[0].message.content)