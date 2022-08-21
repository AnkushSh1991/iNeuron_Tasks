import pymysql as pymysql
from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
import mysql.connector as conn

# creating object of Flask library, so that we can use each method avaialble in flask class
app = Flask(__name__)
#mysql = MySQL(app)

mydb = conn.connect(host="localhost", user="root", passwd="Ewqdsacxz@007")
cur = mydb.cursor()

# app.config['MYSQL_HOST'] ='localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Ewqdsacxz@007'
# app.config['MYSQL_DB'] ='dbpython'


@app.route('/insert_operation', methods = ['GET','POST'])
def DB_operation_insert():
    if (request.method=='POST'):
        empid = int(request.json['empid'])
        empname = (request.json['empname'])
        empmail = (request.json['empmail'])
        empsal = int(request.json['empsal'])
        empatt = int(request.json['empatt'])
        s = f"INSERT INTO dbpython.ineuron1 VALUES({empid},'{empname}','{empmail}',{empsal},{empatt})"
        cur.execute(s)
        mydb.commit()
        cur.close()
        mydb.close()
        result = 'The employee record having empid as ' + str(empid) + ' is  successfully inserted'
        return jsonify(result)


@app.route('/update_operation', methods = ['GET','POST'])
def DB_operation_update():
    if (request.method == 'POST'):
        filter_col = request.json['filter_column']
        filter_value = request.json['filter_value']
        colname = request.json['column_name']
        new_value = request.json['new_value']
        s1 = f"UPDATE dbpython.ineuron1 SET {colname} = {new_value} WHERE {filter_col} = {filter_value}"
        cur.execute(s1)
        mydb.commit()
        cur.close()
        mydb.close()
        result = 'The employee record is  successfully updated'
        return jsonify(result)

@app.route('/delete_operation', methods = ['GET','POST'])
def DB_operation_delete():
    if (request.method == 'POST'):
        filter_col = request.json['filter_column']
        filter_value = request.json['filter_value']
        s2 = f"DELETE FROM dbpython.ineuron1 WHERE {filter_col} = {filter_value}"
        cur.execute(s2)
        mydb.commit()
        cur.close()
        mydb.close()

        result = 'The employee record is successfully deleted'
        return jsonify(result)

@app.route('/fetch_operation', methods = ['GET','POST'])
def DB_operation_fetch():
    if (request.method == 'POST'):
        filter_col = request.json['filter_column']
        filter_value = request.json['filter_value']
        s3 = f"SELECT * FROM dbpython.ineuron1 WHERE {filter_col} = {filter_value}"
        cur.execute(s3)
        l = []
        for i in cur.fetchall():
            l.append(i)
        cur.close()
        mydb.close()
        return jsonify(l)




if __name__ == '__main__':
    app.run()
