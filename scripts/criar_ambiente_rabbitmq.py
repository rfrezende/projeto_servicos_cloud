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


print(f'{datetime.now()} Criando ambiente...')
con = new_connection()
channel = con.channel()

channel.exchange_declare(exchange='transacoes', exchange_type='direct')

# Fila para as transações
channel.queue_declare(queue='transacoes_solicitadas', durable=True)
channel.queue_bind(queue='transacoes_solicitadas', exchange='transacoes', routing_key='solicitar')

# Fila para as notificações de movimentações em conta
channel.queue_declare(queue='transacoes_notificacao', durable=True)
channel.queue_bind(queue='transacoes_notificacao', exchange='transacoes', routing_key='notificar')

con.close()
print(f'{datetime.now()} Ambiente criado.')
