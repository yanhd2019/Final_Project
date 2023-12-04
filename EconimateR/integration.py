from flask import Flask, render_template, request, jsonify, redirect, url_for
from functions import *
import requests

app = Flask(__name__)

data = request.get_json()

@app.route('/')
def index():

    return render_template('chat_page.html')

@app.route('/ask_question', methods=['POST'])
def ask_question():
    question = data['question']

#    excuteAPI(question,final_video_path='./static/final_video.mp4')

    video_id = '_TsyUrSkRqU'

    if video_id:
        # YouTube video embedding
#    embeded_code = ' ''<video width="1280" height="720" controls>
#	<source src="{{ url_for('static',filename='final_video.mp4') }}" type="video/mp4">
#	Your browser does not support the video tag
#</video>'''
        embed_code = f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>'
        answer = f"Video: {embed_code}"
    else:
        answer = f"Question: {question} No Video Generated. Let me try again"

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
