import boto3 as boto
import webbrowser
from time import sleep

# will create ec2 instance ..............

def create_ec2_instance(db_endpoint:str):
    try:
        user_data = """
            #!/bin/bash
            sudo yum update -y
            sudo yum install -y httpd php php-mysqlnd
            sudo service httpd start   
            mkdir ~/.aws && cd ~/.aws
            touch credentials && touch config
            echo "[default]" > credentials
            echo "AWS_ACCESS_KEY_ID = ****************************" >> credentials
            echo "AWS_SECRET_ACCESS_KEY = ***************************" >> credentials
            echo "[default]" > config
            echo "output = json" >> config
            echo "region = ap-south-1" >> config
            aws s3 sync s3://bucketforboto00001  /var/www/html 
            echo '<?php
        define("DB_SERVER", \"""" + db_endpoint + """:3306");
        define("DB_USER", "admin");
        define("DB_PASSWORD", "password1234");
        define("DB_NAME", "feedbackdatabase");

        $conn = new mysqli(DB_SERVER, DB_USER, DB_PASSWORD, DB_NAME);

        if($conn->connect_error){
            die("Connection error: ".$conn->connect_error);
        }

    ?>' > /var/www/html/configuration.php
        """
    
        ec2_cli = boto.client('ec2','ap-south-1')
        ec2_res = boto.resource('ec2','ap-south-1')
        ec2_instance = ec2_res.create_instances(
            InstanceType = 't2.micro',
            KeyName = 'nav',
            UserData = user_data,
            MinCount = 1,
            MaxCount = 1,
            SecurityGroupIds=['sg-0963ca42d1e476186'],
            ImageId = 'ami-076e3a557efe1aa9c',
        )
        print("Amazon ec2 instance created successfully !")
        print(f" response = {ec2_instance} \n")
        waiter = ec2_cli.get_waiter('instance_running')
        waiter.wait(InstanceIds=[ec2_instance[0].id])
        print("\t Instance is in running state :)")
        print(f"\t instance_id: {ec2_instance[0].id}")
        return ec2_instance[0].id
    
    except Exception as error:
        print(f"Amazon ec2 instance could not be created due to error = {error} \n\n")
        return None


# will open dns server of ec2 instance ...................

def OpenDNSserver(instance_id):
    ec2_cli = boto.client('ec2','ap-south-1')
    instance_desc = ec2_cli.describe_instances()["Reservations"]

    for instance_des in instance_desc:
        instance = instance_des["Instances"][0]
        if instance["InstanceId"] == instance_id:
            dns = instance["PublicDnsName"]
            print(f" public dns = {dns}")
            print("\t\t waiting for instance passing status .....")
            for i in range(50):
                print(f"\t\t\t\t progress = {i*2}%\n")
                sleep(1)
            print("\n**************************************************\n\n")
            print("\t\t Opening browser")
            webbrowser.open(dns)


# will create database instance ....................

def create_database_instance():
    try:
        rds_client = boto.client('rds','ap-south-1')
        res = rds_client.create_db_instance(
            DBName = 'feedbackdatabase',
            DBInstanceIdentifier='rdsassignment',
            AllocatedStorage = 6,
            DBInstanceClass='db.t2.micro',
            Engine='mysql',
            PubliclyAccessible=True,
            MasterUsername='admin',
            MasterUserPassword='password1234',
            DBParameterGroupName='customerfeedbackapp',
        )

        print("Amazon mysql rds created successfully !")
        print(f" response = {res} \n")

        waiter = rds_client.get_waiter('db_instance_available')
        waiter.wait(DBInstanceIdentifier='rdsassignment')
        print("Amazon rds instance is running now ...")

        res = rds_client.describe_db_instances(
            DBInstanceIdentifier='rdsassignment',
        )
        endpoint = res['DBInstances'][0]['Endpoint']['Address']
        return endpoint

    except Exception as error:
        print(f"Amazon mysql rds ccould not be created due to error = {error} \n\n")
        return None


if __name__ == "__main__":


    db_endpoint = create_database_instance()
    if(db_endpoint == None):
        exit()
    
    print(f"\n\n{db_endpoint}")

    instance_id = create_ec2_instance(db_endpoint=db_endpoint)

    OpenDNSserver(instance_id=instance_id)

    print("\n\n Thank You \n\n")
