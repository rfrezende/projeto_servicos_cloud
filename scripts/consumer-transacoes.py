# coding=utf-8
###############################################################################
#
# Script para processar as solicitações de transações.
#  - Retira do RabbitMQ e grava no Redis.
#  - Notifica que houve movimentação na conta
# 
# Parte do projeto do módulo Serviços Cloud do treinamento Jornada Digital 
# ADA-Caixa
#
# Autor: Roberto Flavio Rezende
#
import json
import redis
from rabbitmq_connection import new_connection


connection = new_connection()
channel = connection.channel()

r = redis.Redis(host='redis', port=6379, decode_responses=True)

def callback(ch, method, properties, body):
        # Grava a transação no Redis
        transacao = json.loads(body.decode('utf-8').replace("'", '"'))
        r.json().arrappend(transacao['conta'], '$.transacoes', transacao['transacao'])
        
        # Coloca uma mensagem para avisar que a conta teve uma nova transação
        channel.basic_publish(exchange='transacoes', routing_key='notificar', body=transacao['conta'])

channel.basic_consume(queue='transacoes_solicitadas', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
