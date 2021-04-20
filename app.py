from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

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
    return render_template('results.html', url = url)

if __name__ == '__main__':
    app.run(debug=True)