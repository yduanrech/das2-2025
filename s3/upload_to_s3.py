import boto3
import os
from botocore.exceptions import NoCredentialsError

# Configurações do S3
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = "clonacartao"

def upload_file_to_s3(file_path, bucket_name, s3_file_name):
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        s3.upload_file(file_path, bucket_name, s3_file_name)
        print(f"Upload bem-sucedido: {s3_file_name}")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except NoCredentialsError:
        print("Credenciais não disponíveis.")

def upload_directory_to_s3(directory_path, bucket_name):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            s3_file_name = os.path.relpath(file_path, directory_path)
            upload_file_to_s3(file_path, bucket_name, s3_file_name)

if __name__ == "__main__":
    # Caminho da pasta contendo os arquivos HTML, CSS, JS e imagens
    directory_path = "s3/site"
    
    # Realiza o upload de todos os arquivos da pasta para o S3
    upload_directory_to_s3(directory_path, BUCKET_NAME)