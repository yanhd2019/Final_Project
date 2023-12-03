from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat_page.html')

@app.route('/ask_question', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data['question']


    answer=f"Question: {question} Answer:This is a sample answer"

    return jsonify({'answer':answer})

if __name__ == '__main__':
    app.run(debug=True)
