from booksapp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    reviews = db.relationship('Review', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User({self.id}, {self.username})"

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def __repr__(self):
        return f"Review({self.id}, {self.user_id}, {self.book_id})"

class Book(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(40), nullable=False)
     author = db.Column(db.String(40), nullable=False)
     isbn = db.Column(db.String(40), nullable=False)
     year = db.Column(db.Integer, nullable=False)
     reviews = db.relationship('Review', backref='book', lazy=True)

     def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author})"