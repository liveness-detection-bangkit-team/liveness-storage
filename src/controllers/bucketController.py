from flask import jsonify
from src.handler.bucketHandler import (
    list_buckets_with_details,
    check_bucket_exists,
    create_gcs_bucket,
    delete_gcs_bucket,
    json_response
)

# List all buckets with details
def list_buckets_with_details_controllers():
    return list_buckets_with_details()

# Create a bucket
def create_bucket_controllers(request_json):
    bucket_name = request_json.get("bucket_name")
    bucket_location = request_json.get("region")
    # check if bucket already exists
    if check_bucket_exists(bucket_name):
        return jsonify({"status_code": 403, "error": "Bucket already exists!"}), 403
    # create bucket
    isValid, message = create_gcs_bucket(bucket_name, bucket_location)
    # failed to create bucket
    if not isValid:
        return jsonify({"status_code": 400, "error": message}), 400
    # successful creation
    return jsonify({"status_code": 201, "message": message}), 201

# Delete a bucket
def delete_bucket_controllers(request_json):
    bucket_name = request_json.get("bucket_name")
    # delete bucket
    isValid, message = delete_gcs_bucket(bucket_name)
    # failed to delete bucket
    if not isValid:
        return jsonify({"status_code": 404, "error": message}), 404
    # successful deletion
    return jsonify({"status_code": 200, "message": message}), 200

# List all objects in a bucket
def list_objects_controllers(request_json):
    bucket_name = request_json.get("bucket_name")
    # check if bucket exists
    if not check_bucket_exists(bucket_name):
        return jsonify({"status_code": 404, "error": "Bucket not found!"}), 404
    # successful
    return json_response(bucket_name)