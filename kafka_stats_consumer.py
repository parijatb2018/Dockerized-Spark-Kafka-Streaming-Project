from kafka import KafkaConsumer
import time

import mysql.connector

import json

try:

    mydb = mysql.connector.connect(
    host='mysql',
    port='3306',
    database='viz',
    user='root',
    password='password',
    connection_timeout=5
    )

    #print(mydb)

    if mydb.is_connected():

        print('viz db connection successful. \n')

        mycursor = mydb.cursor()

        mycursor.execute('''CREATE TABLE if not exists`bar` (
                            `id` int NOT NULL,
                            `json_dict` longtext,
                            PRIMARY KEY (`Id`)   
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci''')

        mycursor.execute('''select json_dict from bar where id=1''')
        result=mycursor.fetchall()
        print(result)
        if not result:
            mycursor.execute(f'''INSERT INTO bar (id, json_dict) 
                                VALUES (1,NULL)''')
            mydb.commit()


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
            


            print ("%s:%d:%d: key=%s value=%s timestamp=%s"  % (message.topic, message.partition,
                                                message.offset, message.key,
                                                message.value,message.timestamp))

            temp[message.key.decode('utf-8')]=int(message.value.decode('utf-8'))

            sorted_temp=dict(sorted(temp.items()))

            print('temp:',sorted_temp)

            print('str-temp:',json.dumps(temp))

            time.sleep(1)

            # bar=[]   
            # for k,v in sorted_temp.items():
            #     d={}
            #     d['key']=k
            #     d['value']=v
            #     bar.append(d)
            # print(bar)
            mycursor.execute('''select json_dict from bar where id=1''')
            result=mycursor.fetchall()

            print('result-inside-loop:',result)

            if result:
                mycursor.execute(f'''update bar set `json_dict`='{json.dumps(temp)}' where id=1''')
                mydb.commit()

            time.sleep(1)     

except mysql.connector.Error as e:
    print('Error DB connection:',e)

finally:
    if mydb.is_connected() :
        mycursor.close()
        mydb.close()
        print('\n mysql server connection properly closed')


# time.sleep(20)



   
    # bar.append(temp)
    # if 'A' in message.key.decode('utf-8') or 'Z' in message.key.decode('utf-8'):
    #     # print(message.timestamp,':')
    #     print('temp:',temp)

    # print(message.value)

    # print(message.value.decode('utf8'))
# print('not executing code here')
# print('bar:',bar)