import mysql.connector

import json

import time


bar=[] 
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
        
        mycursor.execute('''select json_dict from bar where id=1''')
        result=mycursor.fetchall()[0][0]
        print('result',result)

        dict=json.loads(result)

        print(type(dict))

        print('dict',dict)

        print(dict.items())

        
        # sorted_dict= dict(sorted(dict.items(),key=lambda x:x[0]))

        sorted_dict= sorted(dict.items(),key=lambda x:x[0])
        print(sorted_dict)

        for k,v in sorted_dict:
            d={}
            d['key']=k
            d['value']=v
            bar.append(d)
        print(bar)              

    time.sleep(1)     

except mysql.connector.Error as e:
    print('Error DB connection:',e)

finally:
    if mydb.is_connected() :
        mycursor.close()
        mydb.close()
        print('\n mysql server connection properly closed')