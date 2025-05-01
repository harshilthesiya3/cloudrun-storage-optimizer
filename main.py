from google.cloud import storage

# Replace this with project ID if hardcoding
project = "<project-id>"

def migrate_storage(request):
    request_json = request.get_json(force=True)
    bucket_name = request_json['incident']['resource_name']

    print(f"bucket_name: {bucket_name}")  

    if not bucket_name:
        print("Error: bucket_name is empty")
        return "Invalid bucket name", 400

    storage_client = storage.Client(project)
    bucket = storage_client.get_bucket(bucket_name)
    bucket.storage_class = "NEARLINE"
    bucket.patch()
    return "Bucket migrated successfully", 200
