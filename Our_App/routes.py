from flask import Flask,render_template
from Our_App import app

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
