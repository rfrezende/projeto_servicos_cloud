# coding=utf-8
###############################################################################
#
# Script para criar o ambiente do RabbitMQ
#
# Parte do projeto do módulo Serviços Cloud do treinamento Jornada Digital 
# ADA-Caixa
#
# Autor: Roberto Flavio Rezende
#
from rabbitmq_connection import new_connection
from datetime import datetime

timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
print(f'{timestamp} Criando ambiente...')

con = new_connection()
channel = con.channel()

channel.exchange_declare(exchange='transacoes', exchange_type='direct')

# Fila para as transações
channel.queue_declare(queue='transacoes_solicitadas', durable=True)
channel.queue_bind(queue='transacoes_solicitadas', exchange='transacoes', routing_key='solicitar')

con.close()

timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
print(f'{timestamp} Ambiente criado.')
