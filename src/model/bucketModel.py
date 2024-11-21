import os
import sys
from google.cloud import storage
from google.auth.exceptions import DefaultCredentialsError
from google.cloud.exceptions import NotFound

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Import BUCKET_NAME, BUCKET_LOCATION from the variables.py file
from variables import BUCKET_NAME, BUCKET_LOCATION

# Function to check if a bucket exists
def check_bucket_exists():
    # Initialize the storage client using default credentials (from environment variable)
    storage_client = storage.Client()
    # Check if the bucket exists
    try:
        storage_client.get_bucket(BUCKET_NAME)
        print(f"Bucket '{BUCKET_NAME}' exists.")
        return True  # Bucket exists
    except NotFound:
        print(f"Bucket '{BUCKET_NAME}' does not exist.")
        return False  # Bucket does not exist

# Function to create a new Google Cloud Storage bucket
def create_bucket():
    try:
        # Initialize the storage client using default credentials (from environment variable)
        storage_client = storage.Client()
        # Create a new bucket instance
        bucket = storage_client.bucket(BUCKET_NAME)
        # Set the location for the bucket (optional)
        bucket.create = BUCKET_LOCATION
        # Create the bucket
        bucket = storage_client.create_bucket(bucket)  # This will create the bucket
        print(f"Bucket {bucket.name} created in {bucket.location} location.")
        
    # Handle exceptions
    except DefaultCredentialsError:
        print("Error: Could not authenticate. Please check your GOOGLE_APPLICATION_CREDENTIALS environment variable.")
    except Exception as e:
        print(f"Error creating bucket: {e}")

    # Close the client
    storage_client.close()

# Function to delete a Google Cloud Storage bucket
def delete_gcs_bucket():
    storage_client = storage.Client()

    try:
        bucket = storage_client.bucket(BUCKET_NAME)

        # List and delete all blobs in the bucket
        blobs = bucket.list_blobs()
        for blob in blobs:
            blob.delete()
            print(f"Blob '{blob.name}' deleted.")

        # Now delete the bucket
        bucket.delete()
        print(f"Bucket '{BUCKET_NAME}' deleted successfully.")
    except NotFound:
        print(f"Bucket '{BUCKET_NAME}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

    # Close the client
    storage_client.close()

if not check_bucket_exists():
    create_bucket()