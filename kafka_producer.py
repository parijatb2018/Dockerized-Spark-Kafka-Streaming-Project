print('Hello from kafka producer')

from kafka import KafkaProducer
from kafka.errors import KafkaError
import time

from faker import Faker

producer=KafkaProducer(bootstrap_servers=['kafka:9092'])

fake=Faker()

d={}
while True:
# for name in names:
    name=fake.name()
    print(name)
    name_first_letter=name[0]
    # print(name_first_letter)
    if name_first_letter in d.keys():
        d[name_first_letter]+=1
    else:
        d[name_first_letter]=1
    d_sorted=dict(sorted(d.items()))
    print(d_sorted)
    producer.send('rockthejvm',name.encode('utf-8'))
    
    time.sleep(10)










