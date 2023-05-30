import boto3

if __name__ == "__main__":

    cloud_front = boto3.client("cloudfront","ap-south-1")

    response = cloud_front.create_distribution(
            DistributionConfig={
                "CallerReference": "my-distribution-cdn",
                "DefaultRootObject": "index.html",
                "Origins": {
                    "Quantity": 1,
                    "Items": [
                        {
                            "Id": "bucketforboto00001",
                            "DomainName": "bucketforboto00001.s3.ap-south-1.amazonaws.com",
                            "S3OriginConfig": {"OriginAccessIdentity": ""},
                        },
                    ],
                },
                "DefaultCacheBehavior": {
                    "TargetOriginId": "bucketforboto00001",
                    "ViewerProtocolPolicy": "allow-all",
                    "AllowedMethods": {
                        "Quantity": 1,
                        "Items": [
                            "GET",
                            "HEAD",
                            "POST",
                            "PUT",
                            "PATCH",
                            "OPTIONS",
                            "DELETE",
                        ],
                        "CachedMethods": {
                            "Quantity": 1,
                            "Items": [
                                "GET",
                                "HEAD",
                                "POST",
                                "PUT",
                                "PATCH",
                                "OPTIONS",
                                "DELETE",
                            ],
                        },
                    },
                },
                "Comment": "Hosting website ...",
                "Enabled": True,
            }
        )
    print(response)