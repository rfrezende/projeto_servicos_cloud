import pika
from time import sleep
from datetime import datetime

while True:
    sleep(5)
    print("--------->  ", end="  ")
    print(datetime.now())
