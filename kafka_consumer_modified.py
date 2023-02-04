
from kafka import KafkaConsumer

import time

def consume_message(topic_name):
    consumer = KafkaConsumer(
        bootstrap_servers=['kafka:9092'], auto_offset_reset='latest',
        group_id='first-group'
    )
    consumer.subscribe(topic_name)
    while True:
        try:
            records = consumer.poll(timeout_ms=1000)
            # print(type(records))
            # print(records)
            
            # print(records.items())
            
            time.sleep(5)

            for topic_data, consumer_records in records.items():
                for consumer_record in consumer_records:
                    print('Received message: '+str(consumer_record.key)+'->'+str(consumer_record.value.decode('utf-8')))
            continue
        except Exception as e:
            print(e)
            continue
        
consume_message('stats')