# coding=utf-8
###############################################################################
#
# Script para enviar solicitações de transações para o RabbitMQ
# Parte do projeto do módulo Soluções Nuvem do treinamento Jornada Digital 
# ADA-Caixa
#
import pika
from rabbitmq_connection import new_connection
from time import sleep
from datetime import datetime


print(f'{datetime.now()} iniciando...')
connection = new_connection()
channel = connection.channel()

message_to_send = '{"chave": "valor"}'
propriedades = pika.BasicProperties(content_type='application/json', reply_to='efetivar')

for i in range(500):
    sleep(5)
    channel.basic_publish(exchange='transacoes', routing_key='solicitar', body=message_to_send, properties=propriedades)
    print(f'{datetime.now()} mensagem enviada')

connection.close()
