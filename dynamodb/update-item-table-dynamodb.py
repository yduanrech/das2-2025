import boto3
import time

#Low level API DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    inicio = time.time()
    resposta = dynamodb.update_item(
        TableName = 'cliente',
        Key = {
            'cpf': {'S': '1234567891'}
        },
        UpdateExpression='SET clienteativo = :val',
        ExpressionAttributeValues={
            ':val': {'S':'true'}
        },
        ReturnValues="UPDATE_NEW"
    )
    print(resposta)
except Exception as e:
    print(e)