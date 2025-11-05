import boto3
import base64

def lambda_handler(event, context):
    try:
        bucket_name = event['bucket_name']
        directory_name = event['directory_name']
        file_name = event['file_name']
        file_content_base64 = event['file_content']

        file_bytes = base64.b64decode(file_content_base64)
        s3_client = boto3.client('s3', region_name='us-east-1')

        key=f"{directory_name}/{file_name}"

        s3_client.put_object(
            Bucket=bucket_name, 
            Key=key, 
            Body=file_bytes
            )
        
        url=f"https://{bucket_name}.s3.amazonaws.com/{key}"

        return{
            "statusCode": 200,
            "message": f"Archivo {file_name} subido exitosamente al bucket {bucket_name} en el directorio {directory_name}.",
            "file_url": url
        }


    except Exception as e:
        return {
            'statusCode': 400,
            'message': f'Error en los parámetros de entrada: {str(e)}'
        }
