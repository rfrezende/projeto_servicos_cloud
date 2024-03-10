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


r = redis.Redis(host='redis', port=6379, decode_responses=True, )

criar_conta = lambda x: f'{random.randrange(10000, 99999)}-{random.randrange(1, 9)}'
r.rpush('contas', *[criar_conta('') for i in range(5)])

contas = r.lrange('contas', 0, -1)
print(contas)
for conta in contas:
    r.json().set(conta, '$', {'transacoes': []})
