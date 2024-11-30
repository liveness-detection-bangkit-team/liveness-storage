from flask import Blueprint, request, jsonify
# from src.rateLimiter import is_rate_limited
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
from src.controllers.folderController import (
    create_nested_folders,
    rename_nested_folders,
    delete_nested_folders,
)
# Create a Blueprint for the routes
routes = Blueprint('routes', __name__)

# Example route with rate limiting
@routes.route('/', methods=['GET'])
def get_resource():
    # ip_address = request.remote_addr  # Get the client's IP address
    #  Check if the IP address is rate limited
    # if is_rate_limited(ip_address):
    #     return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
    # If not rate limited, proceed with the request
    return jsonify({"data": "Here is your resource!"})

# ==============================================================================
# List all buckets
@routes.route('/buckets', methods=['GET'])
def get_buckets_route():
    # ip_address = request.remote_addr  # Get the client's IP address
    #  Check if the IP address is rate limited
    # if is_rate_limited(ip_address):
    #     return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
    # If not rate limited, proceed with the request
    return list_buckets_with_details_controllers()

# Create a new bucket
@routes.route('/bucket/create', methods=['POST'])
def create_bucket_route():
    # Get the JSON data from the request
    request_json = request.get_json()
    # ip_address = request.remote_addr  # Get the client's IP address
    #  Check if the IP address is rate limited
    # if is_rate_limited(ip_address):
    #     return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
    # If not rate limited, proceed with the request
    return create_bucket_controllers(request_json)

# Delete a bucket
@routes.route('/bucket/delete', methods=['DELETE'])
def delete_bucket_route():
    # Get the JSON data from the request
    request_json = request.get_json()
    # ip_address = request.remote_addr  # Get the client's IP address
    #  Check if the IP address is rate limited
    # if is_rate_limited(ip_address):
    #     return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
    # If not rate limited, proceed with the request
    return delete_bucket_controllers(request_json)

# List all objects in a bucket
@routes.route('/files', methods=['GET'])
def bucket_list_route():
    # Get the JSON data from the request
    request_json = request.get_json()
    # ip_address = request.remote_addr  # Get the client's IP address
    #  Check if the IP address is rate limited
    # if is_rate_limited(ip_address):
    #     return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
    # If not rate limited, proceed with the request
    return list_objects_controllers(request_json)

# ==============================================================================
# Upload a new file to a bucket
@routes.route('/file/upload', methods=['POST'])
def upload_file_route():
    # ip_address = request.remote_addr  # Get the client's IP address
    #  Check if the IP address is rate limited
    # if is_rate_limited(ip_address):
    #     return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
    # If not rate limited, proceed with the request
    return upload_file_controllers(request)

# Replace a file in a bucket
@routes.route('/file/replace', methods=['PUT'])
def replace_file_route():
    # ip_address = request.remote_addr  # Get the client's IP address
    #  Check if the IP address is rate limited
    # if is_rate_limited(ip_address):
    #     return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
    # If not rate limited, proceed with the request
    return replace_file_controllers(request)

# Rename a file in a bucket
@routes.route('/file/rename', methods=['PUT'])
def rename_file_route():
    # Get the JSON data from the request
    request_json = request.get_json()
    # ip_address = request.remote_addr  # Get the client's IP address
    #  Check if the IP address is rate limited
    # if is_rate_limited(ip_address):
    #     return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
    # If not rate limited, proceed with the request
    return rename_file_controllers(request_json)

# Delete a file from a bucket
@routes.route('/file/delete', methods=['DELETE'])
def delete_file_route():
    # Get the JSON data from the request
    request_json = request.get_json()
    # ip_address = request.remote_addr  # Get the client's IP address
    #  Check if the IP address is rate limited
    # if is_rate_limited(ip_address):
    #     return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
    # If not rate limited, proceed with the request
    return delete_file_controllers(request_json)

# ==============================================================================
# Create a new folder in a bucket
@routes.route('/folder/create', methods=['POST'])
def create_folder_route():
    # Get the JSON data from the request
    request_json = request.get_json()
    # ip_address = request.remote_addr  # Get the client's IP address
    #  Check if the IP address is rate limited
    # if is_rate_limited(ip_address):
    #     return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
    # If not rate limited, proceed with the request
    return create_nested_folders(request_json)

# Rename a folder in a bucket
@routes.route('/folder/rename', methods=['PUT'])
def rename_folder_route():
    # Get the JSON data from the request
    request_json = request.get_json()
    # ip_address = request.remote_addr  # Get the client's IP address
    #  Check if the IP address is rate limited
    # if is_rate_limited(ip_address):
    #     return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
    # If not rate limited, proceed with the request
    return rename_nested_folders(request_json)

# Delete a folder in a bucket
@routes.route('/folder/delete', methods=['DELETE'])
def delete_folder_route():
    # Get the JSON data from the request
    request_json = request.get_json()
    # ip_address = request.remote_addr  # Get the client's IP address
    #  Check if the IP address is rate limited
    # if is_rate_limited(ip_address):
    #     return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
    # If not rate limited, proceed with the request
    return delete_nested_folders(request_json)