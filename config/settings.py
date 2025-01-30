from dotenv import load_dotenv
import os

def configure_environment():
    load_dotenv()

def get_google_api_key():
    return os.getenv("GOOGLE_API_KEY")