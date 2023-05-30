# lab2 readme.md

steps :- 
    1. Created a security group with all required permission via aws website .
    2. Add a user via iam role and give him all required permission via aws website .
    3. Add .aws/credential file to the computer root dir
    4. using nano editor put 
        "[default]"
        "AWS_ACCESS_KEY_ID = user_access_key_id"
        "AWS_SECRET_ACCESS_KEY = user_secret_access_key"

    5. open folder in your terminal
    6. install boto3 via pip ( pip install boto3)
    7. to create a bucket run python -u s3_bucket.py
    8. modifily ec2_instance -> user_data --
            echo "AWS_ACCESS_KEY_ID = ****user_access_id" >> credentials
            echo "AWS_SECRET_ACCESS_KEY = ****user_secret_key_id" >> credentials

    9. to create instance run python -u ec2_instance.py
    

