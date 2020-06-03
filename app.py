from flask import Flask, redirect, render_template, request
from pymongo import MongoClient

client = MongoClient()
db = client.flask_python_tutorial
collection = db.pyt



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/loops')
def loops():
    return render_template('loops.html')

@app.route('/operators', methods = ['GET', 'POST'])
def operators():
    if request.method == 'POST':
        collection.insert_one({
                'title': request.form['title'],
                'description': request.form['description'],
                'symbol': request.form['symbol'],
                'example': request.form['example'],
                'uses': request.form['uses']
        }
        )
        return redirect('/operators')
    opers = collection.find()
    return render_template('operators.html', opers = opers)

