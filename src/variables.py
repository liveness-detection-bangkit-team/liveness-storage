import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
PROJECT_ID = os.getenv("PROJECT_ID")
BUCKET_NAME = os.getenv("CLOUD_BUCKET_NAME")
BUCKET_LOCATION = os.getenv("CLOUD_BUCKET_LOCATION")