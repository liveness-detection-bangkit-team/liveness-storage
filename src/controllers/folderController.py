from flask import jsonify
from src.handler.folderHandler import (
    create_folder,
    rename_folder,
    delete_subfolder
)

# Create nested folders
def create_nested_folders(request_json):
    # Extract the folder names from the request JSON
    bucket_name = request_json.get('bucket_name')
    folder_name = request_json.get('folder_name')
    # Attempt to create the folder
    isValid, message = create_folder(bucket_name, folder_name)
    # failed to create folder
    if not isValid:
        return jsonify({"status_code": 400, "error": message}), 400
    # successful
    return jsonify({"status_code": 201, "message": message}), 201

# Rename nested folders
def rename_nested_folders(request_json):
    # Extract the folder names from the request JSON
    bucket_name = request_json.get('bucket_name')
    old_foldername = request_json.get('old_foldername')
    new_foldername = request_json.get('new_foldername')
    # Attempt to rename the folder
    isValid, message = rename_folder(bucket_name, old_foldername, new_foldername)
    # failed to rename folder    
    if not isValid:
        return jsonify({"status_code": 400, "error": message}), 400    
    # successful
    return jsonify({"status_code": 200, "message": message}), 200

# Delete nested folders
def delete_nested_folders(request_json):
    # Extract the folder names from the request JSON
    bucket_name = request_json.get('bucket_name')
    folder_name = request_json.get('folder_name')
    subfolder_name = request_json.get('subfolder_name')
    # Attempt to delete the folder
    isValid, message = delete_subfolder(bucket_name, folder_name, subfolder_name)
    # failed to delete folder    
    if not isValid:
        return jsonify({"status_code": 400, "error": message}), 400
    # successful
    return jsonify({"status_code": 200, "message": message}), 200    