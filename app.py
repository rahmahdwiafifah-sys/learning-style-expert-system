from flask import Flask, render_template, request

from questions import questions
from rules import calculate_result

from models import db, Result
from recommendations import recommendations

import os


app = Flask(__name__)


# CONFIG DATABASE POSTGRESQL
app.config['SQLALCHEMY_DATABASE_URI'] = (

    f"postgresql://"

    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"

)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# INIT DATABASE
db.init_app(app)


# CREATE TABLE
with app.app_context():
    db.create_all()


# HALAMAN UTAMA
@app.route('/')
def index():

    return render_template('index.html')


# HALAMAN QUIZ
@app.route('/quiz')
def quiz():

    return render_template(
        'quiz.html',
        questions=questions
    )


# HASIL QUIZ
@app.route('/result', methods=['POST'])
def result():

    dominant, percentages = calculate_result(
        questions,
        request.form
    )

    # SIMPAN KE DATABASE
    new_result = Result(

        visual=percentages['visual'],
        auditory=percentages['auditory'],
        kinesthetic=percentages['kinesthetic'],
        dominant=dominant

    )

    db.session.add(new_result)

    db.session.commit()

    return render_template(

        'result.html',
        dominant=dominant,
        percentages=percentages,
        recommendations=recommendations[dominant]

    )


# DASHBOARD BK
@app.route('/dashboard')
def dashboard():

    data = Result.query.all()

    return render_template(
        'dashboard.html',
        data=data
    )

@app.route('/about')
def about():

    return render_template('about.html')

# RUN APP
if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )