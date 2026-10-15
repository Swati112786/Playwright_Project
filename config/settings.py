import os
from pathlib import Path

from dotenv import load_dotenv

# Find the project's root from config/settings.py.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load environment variables from the project's .env file
load_dotenv(PROJECT_ROOT / ".env")

# Read the application URL
BASE_URL = os.getenv("BASE_URL")

if not BASE_URL:
    raise ValueError(
        "BASE_URL is missing. Please check the .env file."
    )
