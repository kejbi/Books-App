from booksapp import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from booksapp.forms import RegistrationForm, LoginForm, SearchingForm
from booksapp.models import User, Book
from flask_login import login_user, current_user, logout_user

def search_books(phrase):
     return Book.query.filter(Book.title.like(f'%{phrase}%') | Book.author.like(f'%{phrase}%') |
                                  Book.isbn.like(f'%{phrase}%')).all()

@app.route('/')
@app.route('/start', methods = ['GET', 'POST'])
def start():
    search_form = SearchingForm()
    if search_form.validate_on_submit():
       return redirect(url_for('search_result', content=search_form.content.data))
        
    return render_template('start.html', search_form = search_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return render_template('start')

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template('start')

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('start'))
        else:
            flash('Login unsuccessfull. Bad email or password', 'fail')

    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('start'))

@app.route('/account')
def account():
    return render_template('start.html')

@app.route('/searchresult/<content>', methods = ['GET', 'POST'])
def search_result(content):
    search_form = SearchingForm()
    if search_form.validate_on_submit():
        return redirect(url_for('search_result', content=search_form.content.data))
    books = search_books(content)
    
    return render_template('search_result.html', books = books, search_form=search_form, content=content)
