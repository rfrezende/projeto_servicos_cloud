
# Projeto do Módulo *Serviços Cloud*

## Treinamento Jornada Digital ADA-Caixa

### Descrição

Projeto proposto para o módulo *Serviços Cloud* do treinamento Jornada Digital ADA-Caixa.  

A solução foi encapsulaad totalmente em containers e executa tudo na ordem correta.

Os scripts executam em containers próprios como a seguir:

- `criar_contas_redis.py`: Cria os objetos JSON com os números das contas e uma lista de transações no Redis. Ele executa e para o container.
- `criar_ambiente_rabbitmq.py`: Cria a exchange, a fila e o biding no RabbitMQ. Ele executa e para o container.
- `criar_ambiente_minio.py`: Cria o bucket no MinIO. Ele executa e para o container.
- `producer_transacoes.py`: Gera transaçoes aleatórias e envia para o RabbitMQ.
- `consumer_transacoes.py`: Consome a fila no RabbitMQ e gera o relatório de fraude, caso seja identificado.

Os demais containers são os serviços do Minio, RabbitMQ, Redis e funções auxiliares.

### Instruções

1. Instalar o Docker e o Docker Compose.  

- https://docs.docker.com/engine/install/  
- https://docs.docker.com/compose/install/  

2. Instalar o git.
    - https://git-scm.com/book/en/v2/Getting-Started-Installing-Git  

3. Clonar o repositório para seu laboratório  

> git clone https://github.com/rfrezende/projeto_servicos_cloud.git

4. Executar o ambiente.  

> cd projeto_servicos_cloud  
> docker-compose up -d  

5. Verificar os logs do container que gera o relatório.  

> docker logs --follow consumer_transacoes
