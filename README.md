# Cloud Storage Flask API
A simple Flask API for managing files and folders in Google Cloud Storage.**

**Build with : Python 3.13**

## Installation
1. Clone this repository.
2. Install the required packages with `pip install -r requirements.txt`.
3. Create a service account key file and download it as a JSON file.
4. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the key file.
5. Run the Flask development server with `flask --debug run -h 0.0.0.0`.

## API Endpoints
### Bucket Management
- **GET /buckets**
    List all buckets with details.

- **POST /bucket/create**
    Create a new bucket with standard storage.
    ##### Request Body (JSON):  
    ```json
    {
        "bucket_name": "your-bucket-name",
        "region": "bucket-region"
    }
    ```

- **DELETE /bucket/delete**
    Delete a bucket.  
    ##### Request Body (JSON):  
    ```json
    {
        "bucket_name": "your-bucket-name"
    }
    ```
---
### File Management
- **GET /files**
    Get all items from the bucket
    ##### Request Body (JSON):  
    ```json
    {
        "bucket_name": "your-bucket-name"
    }
    ```
- **POST /file/upload**  
    Upload a new file to a bucket.  
    ##### Request Body (JSON):  
    ```json
    {
        "bucket_name": "your-bucket-name",
        "folder_name": "your-folder-name",
        "file_name": "your-file-name"
    }
    ```
 
- **PUT /file/replace**  
    Replace an existing file in a bucket.
    ##### Request Body (JSON):  
    ```json
    {
        "bucket_name": "your-bucket-name",
        "folder_name": "your-folder-name",
        "file_name": "your-file-name"
    }
    ```

- **PUT /file/rename**  
    Rename a file in a bucket.  
    ##### Request Body (JSON):
    ```json
    {
        "bucket_name": "your-bucket-name",
        "folder_name": "your-folder-name",
        "old_filename": "old-file-name",
        "new_filename": "new-file-name"
    }
    ```

- **DELETE /file/delete**  
    Delete a file from a bucket.  
    ##### Request Body (JSON): 
    ```json
    {
        "bucket_name": "your-bucket-name",
        "folder_name": "your-folder-name",
        "file_name": "your-file-name"
    }
    ```
 ---
### Folder Management

- **POST /folder/create**  
  Create a new folder in a bucket.  
  **Request Body (JSON):**  
  ```json
  {
    "bucket_name": "your-bucket-name",
    "folder_name": "your-folder-name"
  }
  ```

- **PUT /folder/rename**  
  Rename a folder in a bucket.  
  **Request Body (JSON):**  
  ```json
  {
    "bucket_name": "your-bucket-name",
    "old_foldername": "old-folder-name",
    "new_foldername": "new-folder-name"
  }
  ```

> ### ⚠️ WARNING
> ##### when delete nested folders, you must keep in mind that it will delete all folders if it has no file in it.
 
- **DELETE /folder/delete**  
  Delete a subfolder from a bucket. 
  **Request Body (JSON):**  
  ```json
  {
    "bucket_name": "your-bucket-name",
    "parent_folder": "parent-folder-name",
    "subfolder_name": "sub-folder-name"
  }
  ```

## Environment Variables

The following environment variables are required:

 - `GOOGLE_APPLICATION_CREDENTIALS`: The path to the service account key file.
 - `FLASK_APP`: main.py. The main file of the Flask app.

## Development

 The following environment variables are optional but recommended for development:
 
 * `FLASK_APP`: The name of the Flask app.
 * `FLASK_ENV`: The environment for the Flask app (development, production, etc.).
 * `FLASK_DEBUG`: Whether to enable debug mode for the Flask app.
 
 ## Contributing
 
 Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.
