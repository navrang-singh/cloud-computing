import boto3
import time
import webbrowser


if __name__ == "__main__":

    security_group_id = "sg-0963ca42d1e476186"

    user_data = """
        #!/bin/bash
        sudo yum install -y httpd
        sudo service httpd start    
        mkdir ~/.aws && cd ~/.aws
        touch credentials && touch config
        echo "[default]" > credentials
        echo "AWS_ACCESS_KEY_ID = *******************************" >> credentials
        echo "AWS_SECRET_ACCESS_KEY = ****************************" >> credentials
        echo "[default]" > config
        echo "output = json" >> config
        echo "region = ap-south-1" >> config
        aws s3 sync s3://bucketforboto00001 /var/www/html 
    """

    autoscale_client = boto3.client('autoscaling','ap-south-1')
    cloudwatch_client = boto3.client('cloudwatch','ap-south-1')
    ec2_client = boto3.client('ec2','ap-south-1')

    print("\n\n ****************************************************************\n\n")
    print(f"                             Program Started                            ")
    print("\n\n ****************************************************************\n\n")
    print("\t boto autoscaling client created .....")
    print("\t boto cloudwatch client created .....")
    print("\t boto ec2 client created .....")


    launch_configuration = autoscale_client.create_launch_configuration(
        ImageId = 'ami-06489866022e12a14',
        InstanceType = 't2.micro',
        SecurityGroups = [security_group_id],
        KeyName = 'nav',
        UserData = user_data,
        LaunchConfigurationName = 'launch_config_1',
    )

    print("\t Launch configuration creation is successful ...")

    autoscaling_group = autoscale_client.create_auto_scaling_group(
        AutoScalingGroupName = 'auto_scale_group',
        MaxSize = 15,
        MinSize = 1,
        DesiredCapacity = 1,
        LaunchConfigurationName = 'launch_config_1',
        AvailabilityZones = ['ap-south-1a'],
    )

    print("\t Auto scaling group creation process is successful ...")

    scale_up_policy = autoscale_client.put_scaling_policy(
        AdjustmentType = 'ChangeInCapacity',
        AutoScalingGroupName = 'auto_scale_group',
        PolicyName = 'ScaleUp',
        ScalingAdjustment = 1,
        Cooldown = 180
    )

    print("\t Scale-up policy is created ...")

    scale_down_policy = autoscale_client.put_scaling_policy(
        AdjustmentType = 'ChangeInCapacity',
        AutoScalingGroupName = 'auto_scale_group',
        PolicyName = 'ScaleDown',
        ScalingAdjustment = -1,
        Cooldown = 180        
    )

    print("\t scale down policy is created ...")
    
    up_alarm = cloudwatch_client.put_metric_alarm(
        AlarmName = 'scale_up_alarm',
        AlarmActions=[
            scale_up_policy['PolicyARN']
        ],
        MetricName = 'CPUUtilization',
        Namespace = 'AWS/EC2',
        Dimensions = [
            {
                'Name': 'AutoScalingGroupName',
                'Value': 'auto_scale_group'
            }
        ],
        Period=60,
        Unit='Percent',
        EvaluationPeriods=2,
        DatapointsToAlarm=2,
        Statistic='Average',
        Threshold=70,
        ComparisonOperator='GreaterThanOrEqualToThreshold',
        TreatMissingData='ignore',
    )

    print("\t Up alarm is created ...");

    down_alarm = cloudwatch_client.put_metric_alarm(
        AlarmName='scale_down_alarm',
        AlarmActions=[
            scale_down_policy['PolicyARN']
        ],
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Dimensions=[
            {
                'Name': 'AutoScalingGroupName',
                'Value': 'auto_scale_group'
            }
        ],
        Period = 60,              
        Unit = 'Percent',
        EvaluationPeriods = 2,    
        DatapointsToAlarm = 2,    #
        Statistic = 'Average',
        Threshold = 50,
        ComparisonOperator = 'LessThanOrEqualToThreshold',
        TreatMissingData = 'ignore',  
    )

    print("\t Down alarm is created ...")
    
    print("\t Waiting for instances to come in online ...")

    time.sleep(5)
    ag = autoscale_client.describe_auto_scaling_groups(
        AutoScalingGroupNames=[
            'auto_scale_group'
        ],
    )

    instances = ag['AutoScalingGroups'][0]['Instances']
    print("\n\n\n")
    print(f"\t instances description = {instances}")
    instance_id = instances[0]['InstanceId']

    waiter = ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])
    print(f"\t Instance running now ...., instance id =  {instance_id}")

    reservations = ec2_client.describe_instances()["Reservations"]

    for reservation in reservations:
        instance = reservation["Instances"][0]
        if instance["InstanceId"] == instance_id:
            dns = instance["PublicDnsName"]
            print(f"\t Public dns   = {dns}")
            sec = 20;
            print("\t Waiting 20 sec for files to get loaded")
            while(sec>-1):
                time.sleep(1)
                print(f"                  {sec}                   ")
                sec -= 1

            print("\n\n *********************************************************************\n\n")
            print(f"                             All done opening browser                           ")
            print("\n\n *********************************************************************\n\n")
            time.sleep(3)
            webbrowser.open(dns)

    print(" All done :) ......")