import logging
from flask import Flask, render_template, request, redirect, url_for

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR)

all_books = []


@app.route('/')
def home():
     return render_template("index.html")


@app.route("/add")
def add():
    try:
        # Code that may raise an error
      
         # / 0  # Division by zero to generate an error
        pass

    except Exception as e:
        # Log the error
        # Log the error with details
        logging.error(f"An error occurred: {str(e)}", exc_info=True)
        # Return error message to the user
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500
    


if __name__ == "__main__":
    app.run(debug=True)

