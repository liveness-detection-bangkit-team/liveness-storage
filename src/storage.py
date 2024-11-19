from google.cloud import storage
from google.auth.exceptions import DefaultCredentialsError
from variables import BUCKET_NAME, BUCKET_LOCATION

# Function to create a new Google Cloud Storage bucket
def create_bucket(bucket_name=BUCKET_NAME, location=BUCKET_LOCATION):
    try:
        # Initialize the storage client using default credentials (from environment variable)
        storage_client = storage.Client()
        # Create a new bucket instance
        bucket = storage_client.bucket(bucket_name)
        # Set the location for the bucket (optional)
        bucket.create = location
        # Create the bucket
        bucket = storage_client.create_bucket(bucket)  # This will create the bucket
        print(f"Bucket {bucket.name} created in {bucket.location} location.")
        
    # Handle exceptions
    except DefaultCredentialsError:
        print("Error: Could not authenticate. Please check your GOOGLE_APPLICATION_CREDENTIALS environment variable.")
    except Exception as e:
        print(f"Error creating bucket: {e}")

