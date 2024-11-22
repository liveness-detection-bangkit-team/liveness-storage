# Cloud Storage Flask API Documentation

## Project Overview
This is a Flask-based REST API that provides a complete interface for managing Google Cloud Storage. It allows users to perform operations on buckets, files, and folders through simple HTTP requests.

## Technical Stack
- Python 3.13
- Flask Framework
- Google Cloud Storage
- Environment Variables (.env)

## Core Features
1. Bucket Management
   - List all buckets
   - Create new buckets
   - Delete buckets

2. File Operations
   - List all files
   - Upload files
   - Replace existing files
   - Rename files
   - Delete files

3. Folder Management
   - Create folders
   - Rename folders
   - Delete folders (with nested folder support)

## Project Structure
```bash
project/
├── .env                 # Environment configuration
├── main.py              # Main application file
├── key.json             # Google Cloud credentials
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
├── .gitignore           # Git ignore file
├── tests/               # Test suite
└── src/                 # Source
```

## Setup Instructions
### I. Environment Setup
   1. Clone the repository
   2. Create a Python virtual environment `python -m venv .venv`
   3. Install dependencies: `pip install -r requirements.txt`
   4. Set up Google Cloud credentials:
      - Create a service account and download the JSON key
      - Rename the key to `key.json` and place it in the project root
   5. Configure environment variables in `.env` file
   6. Run the application: `flask --debug run -h 0.0.0.0`

### II. Required Environment Variables
   1. `GOOGLE_APPLICATION_CREDENTIALS`: Points to `key.json`
   2. `FLASK_APP`: Set to main.py

## API Usage Guide

### I. Bucket Operations
1. List Buckets
   - Endpoint: **GET** `/buckets`
   - Returns: List of all available buckets

2. Create Bucket
   - Endpoint: **POST** `/bucket/create`
   - Required `JSON`:
        ```json
        {
            "bucket_name": "string",
            "region": "string"
        }
        ```
   - Creates a new storage bucket

3. Delete Bucket
   - Endpoint: **DELETE** `/bucket/delete`
   - Required `JSON`:
        ```json
        {
            "bucket_name": "string"
        }
        ```
   - Removes specified bucket

### II. File Operations
1. List Files
   - Endpoint: **GET** `/files`
   - Required `JSON`:
        ```json
        {
            "bucket_name": "string"
        }
        ```
   - Lists all files in bucket

2. Upload File
   - Endpoint: **POST** `/file/upload`
   - Required `JSON`:
        ```json
        {
            "bucket_name": "string",
            "folder_name": "string",
            "file_name": "string"
        }
        ```
   - Uploads new file to specified location

3. Replace File
   - Endpoint: **PUT** `/file/replace`
   - Required `JSON`:
        ```json
        {
            "bucket_name": "string", 
            "folder_name": "string", 
            "file_name": "string"
        }
        ```
   - Replaces existing file

4. Rename File
   - Endpoint: **PUT** `/file/rename`
   - Required `JSON`:
        ```json
        {
            "bucket_name": "string", 
            "folder_name": "string", 
            "old_filename": "string", 
            "new_filename": "string"
        }
        ```
   - Renames existing file

5. Delete File
   - Endpoint: **DELETE** `/file/delete`
   - Required `JSON`:
        ```json
        {
            "bucket_name": "string", 
            "folder_name": "string", 
            "file_name": "string"
        }
        ```
   - Removes specified file

### III. Folder Operations
1. Create Folder
   - Endpoint: **POST** `/folder/create`
   - Required `JSON`:
        ```json
        {
            "bucket_name": "string", 
            "folder_name": "string"
        }
        ```
   - Creates new folder

2. Rename Folder
   - Endpoint: **PUT** `/folder/rename`
   - Required `JSON`:
        ```json
        {
            "bucket_name": "string", 
            "old_foldername": "string", 
            "new_foldername": "string"
        }
        ```
   - Renames existing folder

3. Delete Folder
   - Endpoint: **DELETE** `/folder/delete`
   - Required `JSON`:
        ```json
        {
            "bucket_name": "string", 
            "parent_folder": "string", 
            "subfolder_name": "string"
        }
   - Deletes folder and contents

## Important Notes
- Nested folder deletion will remove all empty folders
- All requests require proper JSON formatting
- Service account key must have appropriate permissions
- Development mode can be enabled with `FLASK_DEBUG=1`

## Development Guidelines
1. Use virtual environment for isolation
2. Follow RESTful API principles
3. Test all endpoints before deployment
4. Keep credentials secure
5. Monitor API usage and performance

## Security Considerations
- Store credentials securely
- Use HTTPS in production
- Implement proper authentication
- Regular security audits
- Monitor access logs

This project provides a robust interface for Google Cloud Storage operations while maintaining simplicity and ease of use.

## Error Handling
The API uses standard HTTP status codes for error responses:
- `200: Success`
- `400: Bad Request`
- `404: Not Found`
- `500: Internal Server Error`

## Best Practices
1. Always use environment variables for sensitive information
2. Implement proper authentication and authorization
3. Use meaningful and consistent naming conventions
4. Handle errors gracefully and provide informative error messages
5. Implement logging for better debugging and monitoring
6. Use HTTPS for all API communications
7. Implement rate limiting to prevent abuse

## Testing
- Unit tests are located in the `tests/` directory
- Run tests using: `python -m unittest discover tests`

## Deployment
1. Set up a Google Cloud project
2. Enable Google Cloud Storage API
3. Deploy the application to Google App Engine or your preferred hosting platform
4. Configure environment variables in the deployment environment

## Contributing
1. Fork the repository
2. Create a new branch for your feature
3. Make your changes and write tests
4. Submit a pull request with a clear description of your changes