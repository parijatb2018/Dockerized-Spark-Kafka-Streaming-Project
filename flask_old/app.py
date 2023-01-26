from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np
import random

import mysql.connector

import json

import time
# import socket
# import socketserver
# # import SimpleHTTPServer
# import simple_http_server as SimpleHTTPServer

# class MyServer(socketserver.TCPServer):
#     allow_reuse_address = True

# server=MyServer()

# if server.allow_reuse_address:
#      server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#----------------

# PORT = 5000

# # Absolutely essential!  This ensures that socket resuse is setup BEFORE
# # it is bound.  Will avoid the TIME_WAIT issue

# class MyTCPServer(socketserver.TCPServer):
#     def server_bind(self):
#         self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         self.socket.bind(self.server_address)

# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# httpd = MyTCPServer(("", PORT), Handler)

# # os.chdir("/My/Webpages/Live/here.html")

# httpd.serve_forever()

# # httpd.shutdown() # If you want to programmatically shut off the server


#----------------


app = Flask(__name__)

#Reading data
# data_df = pd.read_csv("static/data/Churn_data.csv")
# churn_df = data_df[(data_df['Churn']=="Yes").notnull()] 

@app.route('/')
def index():
    return render_template('index.html')

# def calculate_percentage(val, total):
#     """Calculates the percentage of a value over a total"""
#     percent = np.round((np.divide(val, total) * 100), 2)
#     return percent

# def data_creation(data, percent, class_labels, group=None):
#     for index, item in enumerate(percent):
#         data_instance = {}
#         data_instance['key'] = class_labels[index]
#         data_instance['value'] = item
#         data_instance['group'] = group
#         data.append(data_instance)

# @app.route('/get_piechart_data')
# def get_piechart_data():
#     contract_labels = ['Month-to-month', 'One year', 'Two year']
#     _ = churn_df.groupby('Contract').size().values
#     class_percent = calculate_percentage(_, np.sum(_)) #Getting the value counts and total

#     piechart_data= []
#     data_creation(piechart_data, class_percent, contract_labels)
#     return jsonify(piechart_data)

@app.route('/get_barchart_data')
def get_barchart_data():
    # tenure_labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
    # churn_df['tenure_group'] = pd.cut(churn_df.tenure, range(0, 81, 10), labels=tenure_labels)
    # select_df = churn_df[['tenure_group','Contract']]
    # contract_month = select_df[select_df['Contract']=='Month-to-month']
    # contract_one = select_df[select_df['Contract']=='One year']
    # contract_two =  select_df[select_df['Contract']=='Two year']
    # _ = contract_month.groupby('tenure_group').size().values
    # mon_percent = calculate_percentage(_, np.sum(_))
    # _ = contract_one.groupby('tenure_group').size().values
    # one_percent = calculate_percentage(_, np.sum(_))
    # _ = contract_two.groupby('tenure_group').size().values
    # two_percent = calculate_percentage(_, np.sum(_))
    # _ = select_df.groupby('tenure_group').size().values
    # all_percent = calculate_percentage(_, np.sum(_))

    # barchart_data = []
    # data_creation(barchart_data,all_percent, tenure_labels, "All")
    # data_creation(barchart_data,mon_percent, tenure_labels, "Month-to-month")
    # data_creation(barchart_data,one_percent, tenure_labels, "One year")
    # data_creation(barchart_data,two_percent, tenure_labels, "Two year")
    # print(jsonify(barchart_data))
    # barchart_data=[{'key': '0-9', 'value': 47.17},
    #                 {'key': '10-19', 'value': 17.81},
    #                 {'key': '20-29', 'value': 12.31},
    #                 {'key': '30-39', 'value': 8.75},
    #                 {'key': '40-49', 'value': 6.37},
    #                 {'key': '50-59', 'value': 4.8},
    #                 {'key': '60-69', 'value': 2.61},
    #                 {'key': '70-79', 'value': 0.18}]
    

    # lowercase=list(map(chr, range(97, 123))) 
    # uppercase=list(map(lambda x: x.upper(),lowercase))
    # d={}    
    # i=0
    # while i<1000:
    #     alphabet=random.choice(uppercase)
        
    #     if alphabet not in d.keys():
    #         d[alphabet]=1
    #     else:
    #         d[alphabet]+=1
            
    #     print(d.items())
    #     i+=1

    # sorted_dic= sorted(d.items(),key=lambda x:x[0])
    
    # from kafka import KafkaConsumer  

    # consumer = KafkaConsumer('stats',
    #                         group_id='second-group',
    #                     bootstrap_servers=['kafka:9092'])
    # print(consumer)
    # temp={}
    # for message in consumer:
    #     print ("%s:%d:%d: key=%s value=%s timestamp=%s"  % (message.topic, message.partition,
    #                                     message.offset, message.key,
    #                                     message.value,message.timestamp))

    #     temp[message.key.decode('utf-8')]=int(message.value.decode('utf-8'))
    #     sorted_temp=dict(sorted(temp.items()))
    #     print(sorted_temp)
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

                   