import os
from dotenv import load_dotenv
from google.cloud import storage

# Load environment variables from .env file
load_dotenv()

# Access environment variables


# Initialize the Google Cloud Storage client
client = storage.Client()
PROJECT_ID = client.project