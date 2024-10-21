from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path

# load environment variables
load_dotenv()
OAI_API_KEY = os.getenv("openai_api_edt")
OAI_ORGANIZATION = os.getenv("openai_organization")
OAI_PROJECT = os.getenv("openai_project")

client = OpenAI(api_key=OAI_API_KEY,
                organization=OAI_ORGANIZATION,
                project=OAI_PROJECT)

user_prompt = "An amazing DJ is playing on the beach in Tulum"
speech_file_path = Path(__file__).parent / "speech.mp3"

response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=user_prompt
)
with open(speech_file_path, "wb") as speech_file:
    speech_file.write(response.content)