const apiUrl = "http://localhost:5000/api";

// Load quizzes from the API
async function loadQuizzes() {
    
    const quizList = document.getElementById("quiz-list");
    try {
        const response = await fetch(`${apiUrl}/quizzes`);
        const data = await response.json();
        console.log(data)
        data.quizzes.forEach(quiz => {
            const listItem = document.createElement("li");
            listItem.innerHTML = `<a href="quiz.html?quiz_id=${quiz.id}">${quiz.title}</a>`;
            quizList.appendChild(listItem);
        });
    } catch (error) {
        console.error("Error loading quizzes:", error);
    }
}

// Load questions for a specific quiz
async function loadQuizQuestions(quizId) {
    const quizForm = document.getElementById("quiz-form");
    try {
        const response = await fetch(`${apiUrl}/quizzes/${quizId}/questions`);
        const data = await response.json();
        
        document.getElementById("quiz-title").textContent = `Quiz: ${quizId}`;
        
        data.questions.forEach((question, index) => {
            const questionDiv = document.createElement("div");
            questionDiv.classList.add("question");

            const questionTitle = document.createElement("p");
            questionTitle.textContent = `${index + 1}. ${question.question_text}`;
            questionDiv.appendChild(questionTitle);
            
            question.choices.forEach(choice => {
                const label = document.createElement("label");
                const radio = document.createElement("input");
                radio.type = "radio";
                radio.name = `question_${question.id}`;
                radio.value = choice.id;
                label.appendChild(radio);
                label.appendChild(document.createTextNode(choice.choice_text));
                questionDiv.appendChild(label);
            });
            quizForm.appendChild(questionDiv);
        });
    } catch (error) {
        console.error("Error loading questions:", error);
    }
}

// Submit quiz and calculate score
async function submitQuiz() {
    const urlParams = new URLSearchParams(window.location.search);
    const quizId = urlParams.get('quiz_id');

    const answers = Array.from(document.querySelectorAll("input[type='radio']:checked")).map(input => ({
        question_id: parseInt(input.name.split('_')[1]),
        choice_id: parseInt(input.value)
    }));

    try {
        const response = await fetch(`${apiUrl}/submit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ quiz_id: quizId, answers: answers })
        });
        const result = await response.json();

        localStorage.setItem('score', result.score);
        localStorage.setItem('totalQuestions', result.total_questions);
        
        window.location.href = "result.html";
    } catch (error) {
        console.error("Error submitting quiz:", error);
    }
}

// Display the result
function displayResult(score, totalQuestions) {
    const resultMessage = document.getElementById("result-message");
    resultMessage.textContent = `You scored ${score} out of ${totalQuestions}!`;
}
