# coding=utf-8
###############################################################################
#
# Script para enviar solicitações de transações para o RabbitMQ
# Parte do projeto do módulo Soluções Nuvem do treinamento Jornada Digital 
# ADA-Caixa
#
import json
import redis
import random
from rabbitmq_connection import new_connection
from time import sleep
from datetime import datetime

r = redis.Redis(host='redis', port=6379, decode_responses=True, )
contas = r.lrange('contas', 0, -1)

print(f'{datetime.now()} iniciando...')
connection = new_connection()
channel = connection.channel()

while True:
    sleep(1)
    conta = contas[random.randint(0, len(contas) - 1)]
    timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    transacao = {'conta': conta, 'transacao': {'valor': 1, 'timestamp': timestamp}}
    channel.basic_publish(exchange='transacoes', routing_key='solicitar', body=str(transacao))
