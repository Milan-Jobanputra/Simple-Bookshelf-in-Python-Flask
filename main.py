import logging
from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify



app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR)

all_books = []


@app.route('/')
def home():
     return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    try: 
       if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        
         
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

