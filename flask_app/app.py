from flask import Flask, jsonify, render_template
import mysql.connector

import json

import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/get_barchart_data')
def get_barchart_data():
   
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

        if mydb.is_connected():

            print('viz db connection successful. \n')

            mycursor = mydb.cursor()
            
            mycursor.execute('''select json_dict from bar where id=1''')
            result=mycursor.fetchall()[0][0]
            print('result',result)

            dict=json.loads(result)

            print('dict',dict)

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
   
    return jsonify(bar)
    
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0',port=80,debug=True)

                   