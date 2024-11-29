from flask import jsonify
import json
from src.handler.bucketHandler import check_bucket_exists
from src.handler.fileHandler import (
    upload_file, 
    replace_file,
    rename_file,
    delete_file
)

# Define routes for file upload, replace, rename, and delete
def upload_file_controllers(request):
    # Ensure there's a file and JSON in the request
    if 'file' not in request.files:
        return jsonify({"status_code": 400, "error": "No file part"}), 400
    # Get the file from the request
    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    # Get the JSON data from the request
    bucket_name = request.form.get("bucket_name")
    folder_name = request.form.get("folder_name")

    # Parse JSON string to dictionary
    try:
        bucket_name = json.loads(bucket_name)  
        folder_name = json.loads(folder_name)
    except json.JSONDecodeError as e:
        return jsonify({"statuc_code": 400, "JSONDecodeError": str(e)}), 400
    except TypeError as e:
        return jsonify({"statuc_code": 400, "TypeError": str(e)}), 400

    # Check if the bucket exists
    isValid = check_bucket_exists(bucket_name)
    if not isValid:
        return jsonify({"status_code": 404, "error": f"Bucket '{bucket_name}' does not exist"}), 404

    # # upload file
    isValid, message = upload_file(bucket_name, folder_name, file)
    # failed to upload file
    if not isValid:
        return jsonify({"status_code": 400, "error": message}), 400
    # successful
    return jsonify({"status_code": 201, "message": message}), 201

def replace_file_controllers(request):
    # Ensure there's a file and JSON in the request
    if 'file' not in request.files:
        return jsonify({"status_code": 400, "error": "No file part"}), 400
    # Get the file from the request
    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    # Get the JSON data from the request
    bucket_name = request.form.get("bucket_name")
    folder_name = request.form.get("folder_name")
    old_filename = request.form.get("old_filename")
    
    # Parse JSON string to dictionary
    try:
        bucket_name = json.loads(bucket_name)  
        folder_name = json.loads(folder_name)
        old_filename = json.loads(old_filename)
    except json.JSONDecodeError as e:
        return jsonify({"statuc_code": 400, "JSONDecodeError": str(e)}), 400
    except TypeError as e:
        return jsonify({"statuc_code": 400, "TypeError": str(e)}), 400

    # Check if the bucket exists
    isValid = check_bucket_exists(bucket_name)
    if not isValid:
        return jsonify({"status_code": 404, "error": f"Bucket '{bucket_name}' does not exist"}), 404

    # replace file
    isValid, message = replace_file(bucket_name, folder_name, file, old_filename)
    # failed to replace file
    if not isValid:
        return jsonify({"status_code": 400, "error": message}), 400
    # successful
    return jsonify({"status_code": 200, "message": message}), 200

def rename_file_controllers(request_json):
    bucket_name = request_json.get("bucket_name")
    folder_name = request_json.get("folder_name")
    old_filename = request_json.get("old_filename")
    new_filename = request_json.get("new_filename")
    # rename file
    isValid, message = rename_file(bucket_name, folder_name, old_filename, new_filename)
    # failed to rename file
    if not isValid:
        return jsonify({"status_code": 400, "error": message}), 400
    # successful
    return jsonify({"status_code": 200, "message": message}), 200

def delete_file_controllers(request_json):
    bucket_name = request_json.get("bucket_name")
    folder_name = request_json.get("folder_name")
    file_name = request_json.get("file_name")
    # delete file
    isValid, message = delete_file(bucket_name, folder_name, file_name)
    # failed to delete file
    if not isValid:
        return jsonify({"status_code": 400, "error": message}), 400
    # successful
    return jsonify({"status_code": 200, "message": message}), 200