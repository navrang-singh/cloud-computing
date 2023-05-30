import boto3
import time

def createNewVersion(application_name):
    try:
        ebsClient = boto3.client('elasticbeanstalk','ap-south-1')
    except Exception as e:
        print(e)
    try:
        ebsClient.create_application_version(
            ApplicationName = application_name,
            VersionLabel='1.0.0',
            Description='Portfolio Website',
            SourceBundle={
                'S3Bucket': 'bucketforboto00001',
                'S3Key': 'portfolio_website.zip'
            },
            AutoCreateApplication=True,
            Process=False
        )
        print('application Created')
    except Exception as e:
        print(e)


def createEnvironment(application_name,environment_name):
    try:
        ebsClient = boto3.client('elasticbeanstalk','ap-south-1')
    except Exception as e:
        print(e)

    try:
        ebsClient.create_environment(
            ApplicationName=application_name,
            EnvironmentName=environment_name,
            Description='Portfolio website using django ..',
            CNAMEPrefix='navrang',
            Tier={
                'Name': 'WebServer',
                'Type': 'Standard',
            },
            VersionLabel='1.0.0',
            SolutionStackName='64bit Amazon Linux 2 v3.3.17 running Python 3.8',
            OptionSettings=[
                {
                    'Namespace': 'aws:autoscaling:launchconfiguration',
                    'OptionName': 'IamInstanceProfile',
                    'Value': 'aws-elasticbeanstalk-ec2-role'
                },
            ],
        )
        print('Environment Created')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    
    application_name = 'assign4portfolio'
    environment_name = 'mycustomenv'
    createNewVersion(application_name)
    print("waiting for 30 sec ...\n")
    createEnvironment(application_name,environment_name)
    print("All done ! ...\n")
