from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql
app = Flask(__name__)
cors = CORS(app)


@app.route('/users', methods=['GET'])
def get_users():
    conn = pymysql.connect(host = "sql6.freesqldatabase.com", user = "sql6468400", password = "9Qc8fnNa4N", db='sql6468400')
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee")
    output = cur.fetchall()
    print(type(output))
    for rec in output:
        print(rec)
    conn.close()
    return jsonify(output)


@app.route('/users', methods=['DELETE'])
def deleteRecord():
    conn = pymysql.connect(host = "sql6.freesqldatabase.com", user = "sql6468400", password = "9Qc8fnNa4N", db='sql6468400')
    cur = conn.cursor()
    emp_id = int(request.args.get('emp_id'))
    query = f"Delete FROM employee WHERE emp_id ={emp_id}"
    res = cur.execute(query)
    conn.commit()
    print(f"Employee with id {emp_id} deleted")
    return {"result" : "Record deleted Succesfully"}


@app.route('/users', methods=['POST'])
def insertRecord():
    conn= pymysql.connect(host = "sql6.freesqldatabase.com",user = "sql6468400",password= "9Qc8fnNa4N",db='sql6468400')
    raw_json = request.get_json()
    emp_name = raw_json["emp_name"]
    emp_phone_number = raw_json["emp_phone_number"]
    emp_city = raw_json["emp_city"]
    sql = f"INSERT INTO employee (emp_id, emp_name, emp_phone_number, emp_city) VALUES (NULL,'{emp_name}','{emp_phone_number}','{emp_city}')"
    print(sql)
    cur= conn.cursor()
    cur.execute(sql)
    conn.commit()
    return {"result" : "Record inserted Succesfully"}


@app.route('/users', methods=['PUT'])
def updateRecord():
    conn= pymysql.connect(host = "sql6.freesqldatabase.com",user = "sql6468400",password= "9Qc8fnNa4N",db='sql6468400')
    raw_json = request.get_json()
    emp_id = raw_json['emp_id']
    emp_name = raw_json["emp_name"]
    emp_phone_number = raw_json["emp_phone_number"]
    emp_city = raw_json["emp_city"]
    sql_update_query=(f"UPDATE employee SET emp_name = '{emp_name}', emp_phone_number = '{emp_phone_number}', emp_city = '{emp_city}' WHERE emp_id = '{emp_id}'")
    cur = conn.cursor()
    cur.execute(sql_update_query)
    conn.commit()
    return {"result" : "Record updated Succesfully"}


if __name__ == "__main__":
    app.run(debug=True)