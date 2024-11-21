from google.cloud import storage
from google.cloud.exceptions import NotFound

# Function to create a new folder in a Google Cloud Storage bucket
def create_folder(bucket_name, folder_name):
    try:
        # Initialize the GCS client
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        
        # Create an empty file with a '/' at the end to represent the folder
        folder_blob = bucket.blob(f"{folder_name}/")  # A folder is just an object with a trailing slash
        # Check if the folder already exists
        if folder_blob.exists():
            return False, f"Folder '{folder_name}' already exists in bucket '{bucket_name}'."
        
        # Upload an empty content (we are just creating the folder structure)
        folder_blob.upload_from_string('')
        
        return True, f"Folder '{folder_name}' created in bucket '{bucket_name}'."
    except Exception as e:
        return False, f"Error occurred: {e}"
    finally:
        # Close the client
        client.close()

# Function to rename a folder in a Google Cloud Storage bucket
def rename_folder(bucket_name, old_folder_name, new_folder_name):
    try:
        # Initialize the GCS client
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        
        # List all blobs with the old folder prefix
        blobs = bucket.list_blobs(prefix=old_folder_name)
        # Check if the old folder exists
        if not bucket.blob(f"{old_folder_name}/").exists():
            return False, f"Folder '{old_folder_name}' not found in bucket '{bucket_name}'."
        # Check if the new folder already exists
        if bucket.blob(f"{new_folder_name}/").exists():
            return False, f"Folder '{new_folder_name}' already exists in bucket '{bucket_name}'."
        
        # Rename all blobs (files) under the old folder to the new folder name
        for blob in blobs:
            # Create new blob with the new folder name (rename the file)
            new_blob_name = blob.name.replace(old_folder_name, new_folder_name, 1)
            new_blob = bucket.blob(new_blob_name)
            
            # Copy the old blob to the new blob (new folder)
            bucket.copy_blob(blob, bucket, new_blob_name)
            
            # Delete the old blob (after copy)
            blob.delete()
        
        return True, f"Folder '{old_folder_name}' renamed to '{new_folder_name}' in bucket '{bucket_name}'."
    except Exception as e:
        return False, f"Error occurred: {e}"
    except NotFound:
        return False, f"Folder '{old_folder_name}' not found in bucket '{bucket_name}'."
    finally:
        # Close the client
        client.close()

# Function to delete a folder and its contents in a Google Cloud Storage bucket
def delete_blobs_in_folder(bucket_name, folder_name):
    """Deletes all blobs (files) in a folder (prefix)."""
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    
    # List all blobs under the folder prefix
    blobs = bucket.list_blobs(prefix=folder_name)
    deleted_files = []
    
    # Delete each blob (file) under the folder
    for blob in blobs:
        blob.delete()
        deleted_files.append(blob.name)
    
    return deleted_files

def delete_subfolder(bucket_name, parent_folder, subfolder_name):
    """Deletes a nested subfolder inside a parent folder in GCS."""
    
    # Ensure the subfolder name ends with '/'
    if not subfolder_name.endswith('/'):
        subfolder_name += '/'
    
    # Construct full folder path (parent folder + subfolder)
    full_folder_name = parent_folder + subfolder_name
    
    # List and delete all blobs (files) under the full folder path
    deleted_files = delete_blobs_in_folder(bucket_name, full_folder_name)
    
    # Prepare the response
    if deleted_files:
        return True, {
            'status': 'success',
            'deleted_files': deleted_files,
            'message': f"Successfully deleted {len(deleted_files)} files/subfolders under '{full_folder_name}'."
        }
    else:
        return True, {
            'status': 'no_files',
            'deleted_files': [],
            'message': f"No files or subfolders found under '{full_folder_name}'."
        }

