from flask import Flask, request, render_template
import requests
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import time

app = Flask(__name__)

API_URL = 'https://api.anthropic.com/v1/complete'
API_KEY = "sk-ant-api03-oKxB8A-JlW37AAA"

@app.route("/chatbot", methods=['GET', 'POST'])
def chatbot():
    answer = ""
    if request.method == 'POST':
        user_input = request.form['prompt']
        prompt = "\n\nHuman:" + user_input + "\n\nAssistant:"

        data = {
          "prompt": prompt,
          "model": "claude-v1.3",
          "max_tokens_to_sample": 5000  
        }

        headers = {
          'Content-Type': 'application/json',
          'x-api-key': API_KEY
        }

        response = requests.post(API_URL, json=data, headers=headers)

        if response.status_code == 200:
            result = response.json()

            answer = result['completion']
            answer = answer.replace('\n', '<br>')

            if result.get('stream'):
                # 打字机效果实现
                pass

            if answer.startswith('```'):
                # 代码高亮实现
                pass

        else:
            answer = "Error: API request failed"

    return render_template('chatbot.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True, port=9999)
