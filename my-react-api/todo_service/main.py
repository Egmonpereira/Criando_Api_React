#https://blog.debugeverything.com/pt/programacao-em-python-aplicativo-flask/
from flask import Flask
from flask import jsonify
from flask.wrappers import Request
from flask_cors import CORS

import json
import mysql.connector

app = Flask(__name__)
app.run(debug=True)
CORS(app)

#read file
with open('tasks.json', 'r') as myfile:
    data=myfile.read()
    
#parse file
obj = json.loads(data)
@app.route('/todo/getall',methods=['GET'])
def getTask():
    return jsonify(obj)

@app.route('/todo/create',methods=['POST'])
def createTask():
    cnx = mysql.connector.connect(user='phpmyadmin', password='Aa@-138205175', host='127.0.0.1:3001')
    
    mycursor = cnx.cursor()
    mycursor.execute("CREATE DATABASE mydatabase")
    req_data = Request.get_json()
    obj.append(req_data)
    return jsonify(req_data)

@app.route('/todo/update',methods=['UPDATE'])
def updateTask():
    return 'Atualizar tarefa'

@app.route('/todo/delete',methods=['DELETE'])
def deleteTask():
    return 'Apagar tarefa'