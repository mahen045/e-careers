from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass123'
app.config['MYSQL_DB'] = 'e_careers'

mysql = MySQL(app)

@app.route('/data', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from employee''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/data', methods=['POST'])
def post_data():
    cur = mysql.connection.cursor()
    id = request.json['id']
    name = request.json['emp_name']
    dept = request.json['emp_dept']
    salary = request.json['emp_sal']
    cur.execute('''INSERT INTO employee (emp_id, emp_name, emp_dept, emp_salary) VALUES(%s, %s, %s, %s)''', (id, name, dept, salary))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message':'Data inserted successfully'})

@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from employee where emp_id = %s''', (id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/data/<int:id>', methods=['PUT'])
def update_data_by_id(id):
    cur = mysql.connection.cursor()
    name = request.json['emp_name']
    dept = request.json['emp_dept']
    cur.execute('''UPDATE employee SET emp_name = %s, emp_dept = %s WHERE emp_id = %s''', (name, dept, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message':'Data updated successfully'})

if __name__ == '__main__':
    app.run(port=5002)