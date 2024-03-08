# coding=utf-8
###############################################################################
#
# Script para criar o ambiente do RabbitMQ
# Parte do projeto do módulo Soluções Nuvem do treinamento Jornada Digital 
# ADA-Caixa
#
from rabbitmq_connection import new_connection
from datetime import datetime


print(f'{datetime.now()} Criando ambiente...')
con = new_connection()
channel = con.channel()
channel.exchange_declare(exchange='transacoes', exchange_type='direct')
channel.queue_declare(queue='transacoes_solicitadas', durable=True)
# channel.queue_declare(queue='transacoes_efetivadas', durable=True)
channel.queue_bind(queue='transacoes_solicitadas', exchange='transacoes', routing_key='solicitar')
# channel.queue_bind(queue='transacoes_efetivadas', exchange='transacoes', routing_key='efetivar')
con.close()
print(f'{datetime.now()} Ambiente criado.')
