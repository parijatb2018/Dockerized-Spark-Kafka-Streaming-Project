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




        consumer = KafkaConsumer('stats',
                                group_id='first-group',auto_offset_reset='latest',enable_auto_commit=True,
                                bootstrap_servers=['kafka:9092'])


        temp={}
        for message in consumer:          


            print ("%s:%d:%d: key=%s value=%s timestamp=%s"  % (message.topic, message.partition,
                                                message.offset, message.key,
                                                message.value,message.timestamp))

            temp[message.key.decode('utf-8')]=int(message.value.decode('utf-8'))

            sorted_temp=dict(sorted(temp.items()))

            mycursor.execute('''select json_dict from bar where id=1''')
            result=mycursor.fetchall()

            print('presently in db:',result)
            print('going to db:',json.dumps(sorted_temp))

            if result:
                mycursor.execute(f'''update bar set `json_dict`='{json.dumps(sorted_temp)}' where id=1''')
                mydb.commit()

            time.sleep(1)     

except mysql.connector.Error as e:
    print('Error DB connection:',e)

finally:
    if mydb.is_connected() :
        mycursor.close()
        mydb.close()
        print('\n mysql server connection properly closed')


