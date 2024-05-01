import boto3

def download_file_from_s3(bucket_name, s3_object_key, local_file_path):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, s3_object_key, local_file_path)
        print(f"File downloaded successfully: {local_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
bucket_name = 'myimages99'
s3_object_key = 'Ranadheer_Are_amazon.pdf'
local_file_path = '/root/downloaded_file.pdf'  # Adjust the path as needed

download_file_from_s3(bucket_name, s3_object_key, local_file_path)

