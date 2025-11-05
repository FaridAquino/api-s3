import boto3

def lambda_handler(event, context):
    try:
        bucket_name= event['bucket_name']
        s3_client = boto3.client('s3', region_name='us-east-1')
        s3_client.create_bucket(Bucket=bucket_name)

        s3_client.put_bucket_ownership_controls(
            Bucket=bucket_name,
            OwnershipControls={
                'Rules': [
                    {
                        'ObjectOwnership': 'BucketOwnerPreferred'
                    },
                ]
            }
        )

        s3_client.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )


        return {
            'statusCode': 200,
            'message': f'Bucket {bucket_name} creado exitosamente.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'message': f'Error al crear el bucket: {str(e)}'
        }

