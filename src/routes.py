from flask import Blueprint, jsonify, request
from src.controllers.bucketController import (
    create_bucket_controllers,
    delete_bucket_controllers,
    list_buckets_with_details_controllers,
    list_objects_controllers,
)
from src.controllers.fileController import (
    upload_file_controllers,
    replace_file_controllers,
    rename_file_controllers,
    delete_file_controllers,
)

# Create a Blueprint for the routes
routes = Blueprint('routes', __name__)

# List all buckets
@routes.route('/buckets', methods=['GET'])
def get_buckets_route():
    return list_buckets_with_details_controllers()

# Create a new bucket
@routes.route('/bucket/create', methods=['POST'])
def create_bucket_route():
    request_json = request.get_json()
    return create_bucket_controllers(request_json)

# Delete a bucket
@routes.route('/bucket/delete', methods=['DELETE'])
def delete_bucket_route():
    request_json = request.get_json()
    return delete_bucket_controllers(request_json)

# List all objects in a bucket
@routes.route('/bucket/list', methods=['GET'])
def bucket_list_route():
    request_json = request.get_json()
    return list_objects_controllers(request_json)

# Upload a new file to a bucket
@routes.route('/file/upload', methods=['POST'])
def upload_file_route():
    request_json = request.get_json()
    return upload_file_controllers(request_json)

# Replace a file in a bucket
@routes.route('/file/replace', methods=['PUT'])
def replace_file_route():
    request_json = request.get_json()
    return replace_file_controllers(request_json)

# Rename a file in a bucket
@routes.route('/file/rename', methods=['PUT'])
def rename_file_route():
    request_json = request.get_json()
    return rename_file_controllers(request_json)

# Delete a file from a bucket
@routes.route('/file/delete', methods=['DELETE'])
def delete_file_route():
    request_json = request.get_json()
    return delete_file_controllers(request_json)
