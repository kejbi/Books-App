import csv
from booksapp import db
from booksapp.models import Book

#before running it make sure you created database

db.drop_all()
db.create_all()

with open('books.csv', mode = 'r') as file:
    reader = csv.reader(file, delimiter=',')
    counter = 0
    for row in reader:
        if not counter == 0:
            book = Book(isbn = row[0], title = row[1], author = row[2], year = int(row[3]))
            db.session.add(book)
        counter += 1
    db.session.commit()

print('Done.')