import boto3
from botocore.exceptions import NoCredentialsError
from typing import List
from classes import *

class S3Uploader:
    def __init__(self, bucket_name: str, aws_access_key: str, aws_secret_key: str):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

    def upload_photos(self, place: Place):
        folder_path = f'grind-set-go/{place.id}/'
        
        for photo in place.gmaps_details.photos:
            try:
                photo_path = f"{folder_path}{photo.name}"
                # Assuming the photos are locally available. Adjust this as necessary for your setup.
                self.s3_client.upload_file(photo.name, self.bucket_name, photo_path)
                print(f"Uploaded {photo.name} to {photo_path}")
            except FileNotFoundError:
                print(f"The file {photo.name} was not found.")
            except NoCredentialsError:
                print("Credentials not available.")
            except Exception as e:
                print(f"An error occurred: {e}")

# Example usage
# if __name__ == "__main__":
#     # Assuming you have a GMapsDetails instance called gmaps_details_instance and a list of photo paths
#     gmaps_details_instance = ...  # Your GMapsDetails instance here
#     place = Place(id=123, gmaps_details=gmaps_details_instance, photos=[])

#     # Replace with your actual bucket name, AWS access key, and AWS secret key
#     bucket_name = 'your-s3-bucket-name'
#     aws_access_key = 'your-aws-access-key'
#     aws_secret_key = 'your-aws-secret-key'

#     uploader = S3Uploader(bucket_name, aws_access_key, aws_secret_key)
#     uploader.upload_photos(place)
