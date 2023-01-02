from kafka import KafkaConsumer
import time

# while True:

consumer = KafkaConsumer('stats',
                        group_id='first-group',
                        bootstrap_servers=['kafka:9092'])

#consumer.printSchema()
# print(type(consumer))


# bar=[]
temp={}
for message in consumer:

    # if message.key.decode('utf-8') not in temp.key():
    #     temp[message.key.decode('utf-8')]=1
    # else:
    #     temp[message.key.decode('utf-8')]+=1
        
    # temp[message.key.decode('utf-8')]=int(message.value.decode('utf-8'))
   
    # # bar.append(temp)
    # print('temp:',temp)
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`        
    


    # print ("%s:%d:%d: key=%s value=%s timestamp=%s"  % (message.topic, message.partition,
    #                                     message.offset, message.key,
    #                                     message.value,message.timestamp))

    temp[message.key.decode('utf-8')]=int(message.value.decode('utf-8'))

    print('temp:',temp)

    time.sleep(5)

    bar=[]   
    for k,v in temp.items():
        d={}
        d['key']=k
        d['value']=v
        bar.append(d)
    print(bar)

    time.sleep(1)
   
    # bar.append(temp)
    # if 'A' in message.key.decode('utf-8') or 'Z' in message.key.decode('utf-8'):
    #     # print(message.timestamp,':')
    #     print('temp:',temp)

    # print(message.value)

    # print(message.value.decode('utf8'))
# print('not executing code here')
# print('bar:',bar)