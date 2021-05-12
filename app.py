import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from analytics.analysis import getAnalysisResults
from analytics.sentiment import sentimentAnalysis
from analytics.frequency import getWordFrequency
from db.models import *

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('results', url = request.form['url']))

    return render_template('index.html')

@app.route('/results')
def results():
    try:
        url = request.args['url']

        record = Result.query.filter_by(url = url).first()
        if record:
            return render_template('results.html', summary = record.summary, sentiment = record.sentiment, display = record.licommon, most_common = record.mcommon)

        text, summary = getAnalysisResults(url)
        sentiment = sentimentAnalysis(text)
        words, most_common = getWordFrequency(text)

        display = ''
        for word in words:
            if word != words[-1]:
                display = display + word + ', '
            else:
                display = display + word
        
        result = Result(url = url, sentiment = sentiment, summary = summary, mcommon = most_common, licommon = display)
        db.session.add(result)
        db.session.commit()

        return render_template('results.html', summary = summary, sentiment = sentiment, display = display, most_common = most_common)

    except:
        return render_template('error.html')
        
if __name__ == '__main__':
    app.run()