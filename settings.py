import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

MODEL_NAME = "gemini-2.5-flash"

MIN_TURNS = 8
MAX_TURNS = 12