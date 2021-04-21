from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from analytics.analysis import getAnalysisResults
from analytics.wordFrequency import getWordFrequency

app = Flask(__name__)
app.secret_key = 'YOUR SECRET KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'YOUR DATABASE URI'
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('results', url = request.form['url']))

    return render_template('index.html')

@app.route('/results')
def results():
    url = request.args['url']
    authors, date, text, summary = getAnalysisResults(url)
    keys, values, total_outcome, greatest_outcome = getWordFrequency(text)
    return render_template('results.html', url = url, authors = authors, date = date, text = text, summary = summary, keys = keys, values = values, total_outcome = total_outcome, greatest_outcome = greatest_outcome)

if __name__ == '__main__':
    app.run(debug=True)