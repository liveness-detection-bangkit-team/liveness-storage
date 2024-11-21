import os
import sys
from google.cloud import storage
from google.cloud.exceptions import NotFound

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Import BUCKET_NAME, BUCKET_LOCATION from the variables.py file
from variables import BUCKET_NAME

# Function to check if a file exists in a Google Cloud Storage bucket
def check_gcs_file_exists(blob_name):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(blob_name)
    # Returns True if the file exists, False otherwise
    return blob.exists()  
    
# Function to add a file to a bucket
def add_file_to_bucket(file_name, folder_name):
    # Initialize the storage client using default credentials (from environment variable)    
    client = storage.Client()
    # Get the bucket
    bucket = client.bucket(BUCKET_NAME)
    # Construct the full path to the file
    file_path = f'file/{file_name}' 
    # Split the file name and extension
    name, ext = os.path.splitext(file_name)
    
    # Check if the file already exists in the bucket
    counter = 0
    while True:
        # ternary operator, if true filename auto increment, otherwise keep the same
        file_name = f'{name}_{counter}{ext}' if counter > 0 else file_name
        # Path in the bucket
        blob_name = f'{folder_name}/{file_name}'
        
        if not check_gcs_file_exists(blob_name):
            break
        counter += 1

    # Create a blob and upload the file
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)

    print(f'File "{file_name}" uploaded successfully in folder "{folder_name}"')

    # Close the client
    client.close()

def replace_file_in_bucket(file_name, folder_name):
    # Initialize the storage client using default credentials (from environment variable)    
    client = storage.Client()
    # Get the bucket
    bucket = client.bucket(BUCKET_NAME)
    # Construct the full path to the file
    file_path = f'file/{file_name}' 

    # Path in the bucket
    blob_name = f'{folder_name}/{file_name}'

    # Create a blob and upload the file
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)

    print(f'File "{file_name}" replaced successfully in folder "{folder_name}"')

    # Close the client
    client.close()

# Function to delete a file from a Google Cloud Storage bucket
def delete_file_in_bucket( folder_name, file_name):
    # Initialize the storage client using default credentials (from environment variable)    
    client = storage.Client()
    # Get the bucket
    bucket = client.bucket(BUCKET_NAME)

    # Path in the bucket
    blob_name = f'{folder_name}/{file_name}'

    # Create a blob and delete the file
    blob = bucket.blob(blob_name)
    try:
        blob.delete()
        print(f"File '{blob_name}' deleted successfully from bucket '{BUCKET_NAME}'.")
    except NotFound:
        print(f"File '{blob_name}' not found in bucket '{BUCKET_NAME}'.")

    # Close the client
    client.close()

add_file_to_bucket('test.txt', 'test')