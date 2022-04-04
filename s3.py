import boto3

#create an object for s3 service
s3_client = boto3.client('s3',
                         aws_access_key_id='***',
                         aws_secret_access_key='***',
                         region_name="ap-south-1")

#creation of bucket
response = s3_client.create_bucket(
    Bucket='aws-s3-demo-afroz123.basha',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    },
)
print(response)


#upload a file to s3 bucket
response = s3_client.put_object(
    Body=open("main.py", "r").read(),
    Bucket='aws-s3-demo-afroz',
    key='index-modified.py'
)
print(response)

#list s3 buckets

response = s3_client.list_buckets()
buckets = response.get("Buckets")
print("Total buckets: {len(buckets)}")
print(buckets)


#list objects

response = s3_client.list_objects(
    Bucket='aws-s3-demo-afroz121'
)
objects = response.get("Contents")
print("Total objects: {len(objects)}")
print(objects)
