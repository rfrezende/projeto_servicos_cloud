#!/usr/bin/env python3
# coding=utf-8
from rabbitmq_connection import new_connection
from datetime import datetime

connection = new_connection()
channel = connection.channel()

def callback(ch, method, properties, body):
        print(f'RECEBIDA:: Exchange: {method.exchange} | Routing key: {method.routing_key} | Payload: {body}')

channel.basic_consume(queue='transacoes_solicitadas', on_message_callback=callback, auto_ack=True)

print(f'{datetime.now()} [*] Aguardando as mensagens.')
channel.start_consuming()
