from booksapp import app
from flask import render_template, url_for

@app.route('/')
@app.route('/start')
def start():
    return render_template('start.html')