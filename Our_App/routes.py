from flask import Flask,render_template
#from Our_App import app

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/singleadd')
def singleAdd():
    return render_template('singleAdd.html')
@app.route('/addAll')
def addAll():
    return render_template('addAll.html')
@app.route('/singledel')
def singledel():
    return render_template('singledel.html')
@app.route('/display')
def display():
    return render_template('display.html')
if __name__ == '__main__':
    app.run(debug = True)