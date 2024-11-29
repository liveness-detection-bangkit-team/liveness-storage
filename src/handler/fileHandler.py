import os
from google.cloud import storage
from google.cloud.exceptions import NotFound

# Function to add a file to a bucket
def upload_file(bucket_name, folder_name, file):
    try:
        # Initialize the storage client using default credentials (from environment variable)    
        client = storage.Client()
        # Get the bucket
        bucket = client.bucket(bucket_name)
        # Split the file name and extension
        name, ext = os.path.splitext(file.filename)
        
        # Check if the file already exists in the bucket
        counter = 0
        while True:
            # If the file already exists, add a counter to the file name
            if counter > 0:
                file_name = f"{name}({counter}){ext}"
            else:
                file_name = file.filename
            
            # If folder_name is empty, use the file name as the blob name
            if folder_name == "":
                blob_name = file_name
            else:
                blob_name = f"{folder_name}/{file_name}"

            # Check if the file already exists in the bucket with the same name
            if not bucket.blob(blob_name).exists():
                break
            counter += 1
        
        # Give response message based on the folder_name
        if folder_name == "":
            response = f"File '{file_name}' uploaded successfully in main folder"
        else:
            response = f"File '{file_name}' uploaded successfully in folder '{folder_name}'"

        # Create a blob and upload the file
        blob = bucket.blob(blob_name)
        blob.upload_from_file(file, content_type=file.content_type)
        
        return True, response
    except Exception as e:
        return False, f"Error occurred: {e}"
    finally:
        # Close the client
        client.close()

def replace_file(bucket_name, folder_name, file, old_filename):
    try:
        # Initialize the storage client using default credentials (from environment variable)    
        client = storage.Client()
        # Get the bucket
        bucket = client.bucket(bucket_name)

        # Path in the bucket
        if folder_name == "":
            blob_name = old_filename
        else:
            blob_name = f"{folder_name}/{old_filename}"

        # Check if the old file exists in the bucket
        if not bucket.blob(blob_name).exists():
            return False, f"File '{blob_name}' does not exist in bucket '{folder_name}'."

        # Create a blob and upload the file
        blob = bucket.blob(blob_name)
        blob.upload_from_file(file, content_type=file.content_type)

        return True, f"File '{file.filename}' success to replace file '{old_filename}'"
    except Exception as e:
        return False, f"Error occurred: {e}"
    finally:
        # Close the client
        client.close()

# Function to rename a file in a Google Cloud Storage bucket
def rename_file(bucket_name, folder_name, old_filename, new_filename):
    try:
        # Initialize the GCS client
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        
        # Construct the old and new file paths in the bucket
        old_name = f"{folder_name}/{old_filename}"
        new_name = f"{folder_name}/{new_filename}"
        
        # Get the blob (object) for the old file
        old_blob = bucket.blob(old_name)
        # Check if the old file exists
        if not old_blob.exists():
            return False, f"The file '{old_name}' does not exist."
        
        # Copy the blob (file) to the new name (location)
        new_blob = bucket.blob(new_name)
        
        # Copy the old blob to the new blob (this is how we "rename" the file)
        bucket.copy_blob(old_blob, bucket, new_name) # !!!!!!!!
        
        # After successful copy, delete the old blob (file)
        old_blob.delete()
        
        return True, f"File renamed from '{old_filename}' to '{new_filename}' in folder '{folder_name}'."
    except Exception as e:
        return False, f"Error occurred: {e}"
    finally:
        # Close the client
        client.close()

# Function to delete a file from a Google Cloud Storage bucket
def delete_file(bucket_name, folder_name, file_name):
    # Initialize the storage client using default credentials (from environment variable)    
    client = storage.Client()
    # Get the bucket
    bucket = client.bucket(bucket_name)

    # Path in the bucket
    blob_name = f'{folder_name}/{file_name}'

    # Create a blob and delete the file
    blob = bucket.blob(blob_name)
    try:
        blob.delete()
        return True, f"File '{blob_name}' deleted successfully from bucket '{bucket_name}'."
    except NotFound:
        return False, f"File '{blob_name}' not found in bucket '{bucket_name}'."
    except Exception as e:
        return False, f"Error occurred: {e}"
    finally:
        # Close the client
        client.close()
