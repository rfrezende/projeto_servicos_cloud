# coding=utf-8
###############################################################################
#
# Script para criar o ambinte no MinIO
#
# Parte do projeto do módulo Serviços Cloud do treinamento Jornada Digital 
# ADA-Caixa
#
# Autor: Roberto Flavio Rezende
#
import json
from minio_connection import new_connection
from datetime import datetime


timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
print(f'{timestamp} Criando o ambiente no MinIO...')

client = new_connection()

bucket_name = 'relatorios-fraudes'

found = client.bucket_exists(bucket_name)
if not found:
    print(f'Bucket {bucket_name} não existe. Criando...')
    client.make_bucket(bucket_name)

    # Permite a leitura dos relatórios sem necessidade de autenticação.
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": [
                        "*"
                    ]
                },
                "Action": [
                    "s3:GetObject"
                ],
                "Resource": [
                    f"arn:aws:s3:::{bucket_name}/*"
                ]
            }
        ],
    }
    
    client.set_bucket_policy(bucket_name, json.dumps(policy))

    timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    print(f'{timestamp} Bucket {bucket_name} criado no MinIO.')

print(f'{timestamp} Ambiente criado no MinIO.')
