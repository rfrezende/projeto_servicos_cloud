#!/usr/bin/env python3
# coding=utf-8
import json
import redis
from rabbitmq_connection import new_connection


connection = new_connection()
channel = connection.channel()

r = redis.Redis(host='redis', port=6379, decode_responses=True)

def callback(ch, method, properties, body):
        transacao = json.loads(body.decode('utf-8').replace("'", '"'))
        r.json().arrappend(transacao['conta'], '$.transacoes', transacao['transacao'])

channel.basic_consume(queue='transacoes_solicitadas', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
