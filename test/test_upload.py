from minio import Minio
from minio.error import S3Error
from conn_minio import connect_minio

# Initialize the MinIO client with your MinIO server details
client = connect_minio()

# Specify the bucket name and file to upload
bucket_name = "bronze"
file_path = "./a.py"
object_name = "a.py"

# Create the bucket if it doesn't exist
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)

try:
    # Upload the file
    client.fput_object(bucket_name, object_name, file_path)
    print(f"'{object_name}' is successfully uploaded to bucket '{bucket_name}'")
except S3Error as exc:
    print("Error occurred:", exc)
