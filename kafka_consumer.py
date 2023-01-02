from kafka import KafkaConsumer

while True:

    consumer = KafkaConsumer('rockthejvm',
                         group_id='first-group',
                         bootstrap_servers=['kafka:9092'])
    
    #consumer.printSchema()
    # print(type(consumer))

    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`

        print('------------------------------------------------------------------------------------------')

        print ("%s:%d:%d: key=%s value=%s timestamp=%s"  % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value,message.timestamp))
    
        # print(message.value)

        # print(message.value.decode('utf8'))