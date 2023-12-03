from flask import Flask, render_template, request, jsonify, redirect, url_for
# from functions import *
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat_page.html')

@app.route('/ask_question', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data['question']

    video_id = '_TsyUrSkRqU'

    if video_id:
        # YouTube video embedding
        embed_code = f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>'
        answer = f"Video: {embed_code}"
    else:
        answer = f"Question: {question} Invalid YouTube URL"

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
