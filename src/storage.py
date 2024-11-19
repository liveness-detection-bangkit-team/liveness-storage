from google.cloud import storage
from src.variables import SA_KEY, PROJECT_ID, BUCKET_NAME

# Replace 'your-project-id' and 'path/to/key.json' with your actual values
client = storage.Client.from_service_account_json(SA_KEY, project=PROJECT_ID)

# Create a new bucket if it doesn't exist already
bucket = client.bucket(BUCKET_NAME)
bucket.create()

# Upload a local file to the bucket
blob = bucket.blob('your-file-name.txt')
blob.upload_from_filename('path/to/local/file.txt')

# Download a file from the bucket
blob = bucket.blob('your-file-name.txt')
blob.download_to_filename('path/to/local/file.txt')

# Delete a file from the bucket
blob = bucket.blob('your-file-name.txt')
blob.delete()

# List all blobs in the bucket
blobs = bucket.list_blobs()
for blob in blobs:
  print(blob.name)
