from flask import jsonify
from src.model.fileModel import (
    upload_file, 
    replace_file,
    rename_file,
    delete_file
)

# Define routes for file upload, replace, rename, and delete
def upload_file_controllers(request_json):
    bucket_name = request_json.get("bucket_name")
    file_name = request_json.get("file_name")
    folder_name = request_json.get("folder_name")
    # upload file
    isValid, message = upload_file(bucket_name, folder_name, file_name)
    # failed to upload file
    if not isValid:
        return jsonify({"status_code": 400, "error": message}), 400
    # successful
    return jsonify({"status_code": 201, "message": message}), 201

def replace_file_controllers(request_json):
    bucket_name = request_json.get("bucket_name")
    file_name = request_json.get("file_name")
    folder_name = request_json.get("folder_name")
    # replace file
    isValid, message = replace_file(bucket_name, folder_name, file_name)
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