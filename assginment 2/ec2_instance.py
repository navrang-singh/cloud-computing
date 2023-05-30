import boto3
import webbrowser
import time


if __name__=="__main__":


    #creating ec2 client
    ec2 = boto3.client('ec2','ap-south-1')
    print('\tec2 client created successfully !')


    # creating key-value pair:
    res = ec2.create_key_pair(KeyName = 'nav')
    print("\tkey created successfully !")
    print(f" key = {res['KeyMaterial']}")

    # storing key into pem file
    file = open('nav.pem','w')
    file.write(res['KeyMaterial'])
    file.close
    print("\tnav.pem created successfully !")

    #ec2 resources_type
    ec2_resources = boto3.resource('ec2','ap-south-1')

    #script to be run on instance
    user_data = """
        #!/bin/bash
        sudo su
        yum update -y
        yum install httpd -y
        mkdir ~/.aws && cd ~/.aws
        touch credentials && touch config
        echo "[default]" > credentials
        echo "AWS_ACCESS_KEY_ID = ****user_access_id" >> credentials
        echo "AWS_SECRET_ACCESS_KEY = ****user_secret_key_id" >> credentials
        echo "[default]" > config
        echo "output = json" >> config
        echo "region = ap-south-1" >> config
        service httpd start
        chown -R $USER:$USER /var/www
        aws s3 sync s3://bucketforboto3267476 /var/www/html
    """

    print("\tcreating ec2.micro instance .... ")
    ec2_machine = ec2_resources.create_instances(
        ImageId = 'ami-076e3a557efe1aa9c',
        MaxCount = 1,
        MinCount = 1,
        KeyName = 'nav',
        SecurityGroupIds=['sg-0963ca42d1e476186'],
        UserData=user_data,
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/xvda',
                'Ebs': {
                    'DeleteOnTermination': True,

                },
            },
        ],
        InstanceType='t2.micro'
    )

    # waiting for instance running state
    waiter = ec2.get_waiter('instance_running')
    waiter.wait(InstanceIds=[ec2_machine[0].id])
    print("\t Instance is in running state :)")
    print(f"\t instance_id: {ec2_machine[0].id}")

    # fetching instance discription
    instance_desc = ec2.describe_instances()["Reservations"]

    # Open DNS in browser
    for instance_des in instance_desc:
        instance = instance_des["Instances"][0]
        if instance["InstanceId"] == ec2_machine[0].id:
            dns = instance["PublicDnsName"]
            print(f" public dns = {dns}")
            print("\t\t waiting for instance passing status .....")
            time.sleep(50)
            print("\t\t Opening browser")
            webbrowser.open(dns)

    print("\n\n\t all done :) !!!")


