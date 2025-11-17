import os, boto3

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"] 
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]

def upload_file_to_s3(file_name, user_id):
    s3_client = boto3.client(service_name="s3", region_name="us-east-1", aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    bucket_name = "compression-interpretability"
    object_name = f"uploads/{user_id}/{file_name}"
    
    EXPIRATION_TIME_IN_SECONDS = 3600

    presigned_url = s3_client.generate_presigned_url(
        'put_object',
        Params={
            'Bucket': bucket_name,
            'Key': object_name,
        },
        ExpiresIn=EXPIRATION_TIME_IN_SECONDS
    )


    upload_info = {
        "presigned_url": presigned_url,
        "object_name": object_name,
    }

    return upload_info

