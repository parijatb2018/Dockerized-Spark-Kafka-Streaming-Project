print('Hello from kafka producer')

# while True:
#     print('running producer')

from kafka import KafkaProducer
from kafka.errors import KafkaError
import time

from faker import Faker

producer=KafkaProducer(bootstrap_servers=['kafka:9092'])

# future=producer.send('rockthejvm',b'hello from kafka producer')

# try:
#     record_metadata = future.get(timeout=10)
# except KafkaError:
#     # Decide what to do if produce request failed...
#     log.exception()
#     pass
# # Successful result returns assigned partition and offset
# print (record_metadata.topic)
# print (record_metadata.partition)
# print (record_metadata.offset)

# time.sleep(5)

fake=Faker()
# names=['Ajay','Raghav','Suvo','Ashim','Raju','Tanmoy','Kamal','Satyajit']
# a2,r2,s2,t1,k1
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

# import os

# ips=['kafka 9092','kafka 9093','kafka']

# for ip in ips:
#     response = os.popen(f"ping -c 1 {ip} ").read()
#     print(response)








