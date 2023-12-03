function fetch_answer() {
    console.log("the button is clicked")
    const questionText = document.getElementById('chat_input').value;

    // QuestionContainer pops up when the button is clicked
    var QuestionContainer = document.getElementById('QuestionContainer');
    QuestionContainer.style.display = 'block';

    var QuestionContainer = document.getElementById('AnswerContainer');
    AnswerContainer.style.display = 'block';

    //Insert the user's q into the <p>tag
    var userMessage = document.getElementById('userQuestion');
    userMessage.textContent = questionText;

    fetch('/ask_question', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: questionText }),
    })
    .then(response => response.json())
    .then(data => {
        const answerContainer = document.getElementById('answerContainer');
        answerContainer.innerHTML = `<p>Answer: ${data.answer}</p>`;
    })
    .catch(error => {
        console.error('Error fetching answer:', error);
    });
}


