function fetch_answer() {
    console.log("the button is clicked")
    const questionText = document.getElementById('chat_input').value;

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
        