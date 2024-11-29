import json
from flask import jsonify
from collections import defaultdict
from google.cloud import storage
from google.auth.exceptions import DefaultCredentialsError
from google.cloud.exceptions import NotFound

# Function to list buckets with details
def list_buckets_with_details():
    # Initialize the Google Cloud Storage client
    client = storage.Client()
    # List all buckets in your project
    buckets = client.list_buckets()
    # Iterate through the buckets and print their details
    response = []
    for bucket in buckets:
        response.append({
            "bucket_name": bucket.name,
            "location": bucket.location,
            "storage_class": bucket.storage_class,
            "created": bucket.time_created,
        })
        
    # Close the client
    client.close()

    return jsonify({f"Buckets in '{client.project}' ": response})

# Function to check if a bucket exists
def check_bucket_exists(bucket_name):
    # Initialize the storage client using default credentials (from environment variable)
    storage_client = storage.Client()
    # Check if the bucket exists
    try:
        storage_client.get_bucket(bucket_name)
        return True  # Bucket exists
    except:
        return False  # Bucket does not exist

# Function to create a new Google Cloud Storage bucket
def create_gcs_bucket(bucket_name, bucket_location):
    try:
        # Initialize the storage client using default credentials (from environment variable)
        storage_client = storage.Client()
        # Create a new bucket instance
        bucket = storage_client.bucket(bucket_name)
        # Set the location for the bucket (optional)
        bucket.location = bucket_location
        # Create the bucket
        bucket = storage_client.create_bucket(bucket)  # This will create the bucket
        return True, f"Bucket {bucket.name} created in {bucket.location} location."
    # Handle exceptions
    except DefaultCredentialsError:
        return False, "Could not authenticate. Please check your GOOGLE_APPLICATION_CREDENTIALS environment variable."
    except Exception as e:
        return False, f"Error creating bucket: {e}"
    finally:
        # Close the client
        storage_client.close()

# Function to delete a Google Cloud Storage bucket
def delete_gcs_bucket(bucket_name):
    try:
        # Initialize the storage client using default credentials (from environment variable)
        storage_client = storage.Client()
        # Get the bucket
        bucket = storage_client.bucket(bucket_name)

        # List and delete all blobs in the bucket
        blobs = bucket.list_blobs()
        for blob in blobs:
            blob.delete()

        # Now delete the bucket
        bucket.delete()
        return True, f"Bucket '{bucket_name}' deleted successfully."
    except NotFound:
        return False, f"Bucket '{bucket_name}' not found."
    except Exception as e:
        return False, f"Error occurred: {e}"
    finally:
        # Close the client
        storage_client.close()

# Function to list files and folders in a Google Cloud Storage bucket
def list_files_and_folders(bucket_name):
    # Initialize the GCS client
    client = storage.Client()
    # To store the tree-like structure of files and folders
    tree = defaultdict(list)
    # List all objects in the bucket
    blobs = client.list_blobs(bucket_name)
    
    # Organize the objects into a tree-like structure
    for blob in blobs:
        # Split the file path by '/' to create the tree structure
        parts = blob.name.split('/')
        folder = parts[0] + '/' # First part is the folder
        if len(parts) > 1:
            tree[folder].append('/'.join(parts[1:]))  # Append subfiles or subfolders
    
    # Convert defaultdict to a regular dict for JSON serialization
    return dict(tree)

# Function to convert the tree structure to a JSON response
def json_response(bucket_name):
    # Get the file and folder tree structure
    tree = list_files_and_folders(bucket_name)
    
    # Convert the tree structure to a JSON response (string)
    return json.dumps(tree, indent=4)