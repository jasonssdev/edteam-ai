from openai import OpenAI
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()
OAI_API_KEY = os.getenv("openai_api_edt")
OAI_ORGANIZATION = os.getenv("openai_organization")
OAI_PROJECT = os.getenv("openai_project")

client = OpenAI(api_key=OAI_API_KEY,
                organization=OAI_ORGANIZATION,
                project=OAI_PROJECT)

user_prompt = "a playing DJ in a beach in Tulum"

response = client.images.generate(
    model="dall-e-3",
    prompt=user_prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)
image_url = response.data[0].url
print(image_url)
