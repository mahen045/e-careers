from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import cross_origin
import mysql.connector
app = Flask(__name__)
# Database connection configuration
def create_connection():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'pass123',
        database = 'e_careers'
    )
    return connection    
#mysql = MySQL(app)
@app.route('/data', methods=['GET'])
@cross_origin(origins='*')
def get_data():
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    cur.execute('''SELECT * from employee''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/data', methods=['POST'])
def post_data():
    #cur = mysql.connection.cursor()
    connection = create_connection()
    cur = connection.cursor()
    id = request.json['id']
    name = request.json['emp_name']
    dept = request.json['emp_dept']
    salary = request.json['emp_sal']
    cur.execute('''INSERT INTO employee (emp_id, emp_name, emp_dept, emp_salary) VALUES(%s, %s, %s, %s)''', (id, name, dept, salary))
    #mysql.connection.commit()
    cur.close()
    return jsonify({'message':'Data inserted successfully'})

# POST /api/submit
# Accepts a JSON payload containing the quiz ID and answers,
# then calculates the score. The request body should look like this:
# {
#     "quiz_id": 1,
#     "answers": [
#         {"question_id": 1, "choice_id": 2},
#         {"question_id": 2, "choice_id": 5}
#     ]
# } 
@app.route('/api/submit', methods=['POST'])
def post_data():
    #cur = mysql.connection.cursor()
    connection = create_connection()
    cur = connection.cursor()
    answers = request.json['answers']
    score = 0
    #Check whether answer is correct or not
    for answer in answers:
        question_id = answer['question_id']
        choice_id = answer['choice_id']
        cur.execute("SELECT is_correct FROM choices where id = %s and question_id = %s",(choice_id, question_id))
        result = cur.fetchone()
        if result:
            score += 1
    return jsonify({"score":score})         
    

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