from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_restful import Api, Resource
from flask_cors import cross_origin
import config

app = Flask(__name__)
app.config.from_object(config)
mysql = MySQL(app)
api = Api(app)

# Endpoint: List all quizzes

class QuizList(Resource):
    @cross_origin(origins= '*') 
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, title, description FROM quizzes")
        quizzes = cur.fetchall()
        return jsonify({"quizzes": quizzes})

# Endpoint: Get questions and choices for a specific quiz
 
class QuizQuestions(Resource):
    @cross_origin(origins= '*')
    def get(self, quiz_id):
        cur = mysql.connection.cursor()
        
        # Fetch questions
        cur.execute("SELECT id, question_text FROM questions WHERE quiz_id = %s", (quiz_id,))
        questions = cur.fetchall()
        
        # Fetch choices for each question
        for question in questions:
            cur.execute("SELECT id, choice_text FROM choices WHERE question_id = %s", (question['id'],))
            question['choices'] = cur.fetchall()
        
        return jsonify({"questions": questions})

# Endpoint: Submit answers and calculate the score

@app.route('/api/submit', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*')
def post():
    data = request.get_json()
    quiz_id = data.get('quiz_id')
    answers = data.get('answers')  # Expected format: [{"question_id": ..., "choice_id": ...}, ...]

    cur = mysql.connection.cursor()
        
    score = 0
    total_questions = 0
        
    # Validate answers
    for answer in answers:
        question_id = answer['question_id']
        choice_id = answer['choice_id']
            
    # Check if the selected choice is correct
        cur.execute(
            "SELECT is_correct FROM choices WHERE id = %s AND question_id = %s",
            (choice_id, question_id)
        )
        result = cur.fetchone()
            
        if result and result['is_correct']:
            score += 1
            
        total_questions += 1
        
    return jsonify({"score": score, "total_questions": total_questions})

# Register API resources
api.add_resource(QuizList, '/api/quizzes')
api.add_resource(QuizQuestions, '/api/quizzes/<int:quiz_id>/questions')
#api.add_resource(SubmitQuiz, '/api/submit')

if __name__ == "__main__":
    app.run()