import boto3

def lambda_handler(event, context):
    try:
        bucket_name = event['body']['bucket_name']
        directory_name = event['body']['directory_name']
        s3_client = boto3.client('s3', region_name='us-east-1')

        s3_client.put_object(Bucket=bucket_name, Key=(directory_name+'/'))

        return {
            'statusCode': 200,
            'message': f'Directorio {directory_name} creado exitosamente en el bucket {bucket_name}.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'message': f'Error al crear el directorio: {str(e)}'
        }
