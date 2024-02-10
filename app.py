# app.py
from flask import Flask, render_template
from quotes_data import quotes_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quotes/<category>')
def show_quotes(category):
    if category in quotes_data:
        return render_template('quotes.html', category=category.capitalize(), quotes=quotes_data[category])
    else:
        return render_template('error.html', message='Category not found')

if __name__ == '__main__':
    app.run(debug=True)
