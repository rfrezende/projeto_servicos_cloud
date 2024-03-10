# coding=utf-8
###############################################################################
#
# Script para criar as contas no Redis
#
# Parte do projeto do módulo Serviços Cloud do treinamento Jornada Digital 
# ADA-Caixa
#
# Autor: Roberto Flavio Rezende
#
import redis
import random
from datetime import datetime

r = redis.Redis(host='redis', port=6379, decode_responses=True, )

timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
print(f'{timestamp} Criando contas no Redis...')

quantidade_de_contas = 10
criar_conta = lambda x: f'{random.randrange(10000, 99999)}-{random.randrange(1, 9)}'  # Função para gerar o número da conta
lista_contas = [criar_conta(None) for i in range(quantidade_de_contas)]
r.rpush('contas', *lista_contas)

contas = r.lrange('contas', 0, -1)  # Recupera a lista de contas geradas no Redis
print(contas)

for conta in contas:
    r.json().set(conta, '$', {'transacoes': []})

timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
print(f'{timestamp} Contas criadas.')