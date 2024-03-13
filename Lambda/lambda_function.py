import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
   
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    obj = s3.get_object(Bucket=bucket, Key=key)

    print('Contenido del objeto:', obj['Body'].read())

    return {
        'statusCode': 200,
        'body': json.dumps('¡Objeto procesado correctamente!')
    }
