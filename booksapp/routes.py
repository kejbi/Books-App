from booksapp import app
from flask import render_template, url_for, flash
from booksapp.forms import RegistrationForm

@app.route('/')
@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
    return render_template('register.html', form = form)