import logging
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)

# CREATE DATABASEP
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR)

#all_books = []


@app.route('/')
def home():
     ##READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_books = result.scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    try: 
       if request.method == "POST":
        new_book = Book(
            
            title= request.form["title"],
            author= request.form["author"],
            rating= request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        #all_books.append(new_book)
        
         
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home'))
      
        

    except Exception as e:
        # Log the error
        # Log the error with details
        logging.error(f"An error occurred: {str(e)}", exc_info=True)
        # Return error message to the user
        #return jsonify({'error': f"An error occurred: {str(e)}"}), 500

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

