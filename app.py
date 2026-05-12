from flask import Flask, render_template, request

from questions import questions
from rules import calculate_result

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quiz')
def quiz():
    return render_template(
        'quiz.html',
        questions=questions
    )


@app.route('/result', methods=['POST'])
def result():

    dominant, percentages = calculate_result(
        questions,
        request.form
    )

    return render_template(
        'result.html',
        dominant=dominant,
        percentages=percentages
    )


if __name__ == '__main__':
    app.run(debug=True)