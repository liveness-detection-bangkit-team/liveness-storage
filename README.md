# Cloud Storage Flask API

> [!IMPORTANT]
>
> - In development progress

A simple Flask API for managing files in Google Cloud Storage.

### Installation

1. Clone this repository.
2. Install the required packages with `pip install -r requirements.txt`.
3. Create a service account key file and download it as a JSON file.
4. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the key file.
5. Run the Flask development server with `python main.py`.

## API Endpoints

#### GET /files

Get a list of all files in the storage bucket.

#### GET /files/:filename

Get a file from the storage bucket.

#### POST /files

Upload a file to the storage bucket.

#### DELETE /files/:filename

Delete a file from the storage bucket.

## Environment Variables

The following environment variables are required:

* `GOOGLE_APPLICATION_CREDENTIALS`: The path to the service account key file.
* `CLOUD_BUCKET_NAME`: The name of the storage bucket.
* `CLOUD_BUCKET_LOCATION`: The location of the storage bucket.

## Development

The following environment variables are optional but recommended for development:

* `FLASK_APP`: The name of the Flask app.
* `FLASK_ENV`: The environment for the Flask app (development, production, etc.).
* `FLASK_DEBUG`: Whether to enable debug mode for the Flask app.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
