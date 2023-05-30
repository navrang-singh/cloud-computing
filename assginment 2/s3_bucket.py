import boto3


if __name__ == "__main__":

    # s3 client
    s3 = boto3.client('s3')
    print("\tboto s3 client initialized !")

    #creating bucket
    res = s3.create_bucket(Bucket = "bucketforboto3267476",CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'})
    print("\tbucket created !")
    print(f"\tresponce = {res}")
    print('\n')

    # uploading index.html
    response = s3.upload_file('index.html','bucketforboto3267476','index.html',ExtraArgs={'ACL': 'public-read'})
    if(response == None):
        print("\tindex file uploaded successfully !")
    else:
        print("\tindex file upload failed! ")

    # uploading style.css
    response = s3.upload_file('style.css','bucketforboto3267476','style.css',ExtraArgs={'ACL': 'public-read'})
    if(response == None):
        print("\tcss file uploaded successfully !")
    else:
        print("\tcss file upload failed! ")
    