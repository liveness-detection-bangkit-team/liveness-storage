import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
SA_KEY = os.getenv("SA_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")

# Replace 'your-bucket-name' with your actual bucket name
BUCKET_NAME = "your-bucket-name"