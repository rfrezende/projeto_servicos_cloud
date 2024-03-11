# coding=utf-8
###############################################################################
#
# Script para gerar os relat'rios de fraude.
#  - Verifica no RabbitMQ as contas com transações efetuadas.
#  - Pega as transações no Redis
#  - Avalia se houve fraude
#  - Salva o relatório no Minio e imprime a URL
# 
# Parte do projeto do módulo Serviços Cloud do treinamento Jornada Digital 
# ADA-Caixa
#
# Autor: Roberto Flavio Rezende
#
import json
import redis
from rabbitmq_connection import new_connection as new_rabbit
from minio_connection import new_connection as new_minio


minio_client = new_minio()
rabbitmq_client = new_rabbit()
channel = rabbitmq_client.channel()
redis_client = redis.Redis(host='redis', decode_responses=True)

def callback(ch, method, properties, body):
    nu_conta = body.decode('utf-8')
    conta = redis_client.json().get(nu_conta, 'transacoes')
    print(json.dumps(conta))
    exit()

channel.basic_consume(queue='transacoes_notificacao', on_message_callback=callback, auto_ack=True)
channel.start_consuming()