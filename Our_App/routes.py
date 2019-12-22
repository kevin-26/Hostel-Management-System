from flask import Flask,render_template,request
#from Our_App import app
import sqlite3
conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE if not exists hostel_record (room_no INTEGER, name TEXT, roll_no INTEGER UNIQUE, age INTEGER,gender TEXT, branch TEXT)')

print("Table created successfully")


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/about',methods=['POST'])
def about():
    return render_template('about.html')
@app.route('/singleadd',methods=['POST'])
def singleadd():
    return render_template('singleadd.html')
@app.route('/singleadd/dataInput',methods = ['POST'])
def dataInput():
    try:
        name = request.form['nm']
        age = request.form['age']
        gender = request.form['gen']
        branch = request.form['bra']
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO hostel_record (room_no,name,roll_no,age,gender,branch)VALUES (?,?,?,?,?,?)",(302,name,2,age,gender,branch) )
            con.commit()
    except:
        conn.rollback()
    finally:
        conn.close()
        return "done"
@app.route('/addAll',methods=['POST'])
@app.route('/addAll')
def addAll():
    return "hello"
    
@app.route('/singledel')
def singledel():
    return render_template('singledel.html')
@app.route('/display',methods=['POST'])
def display():

    cony = sqlite3.connect("database.db")
    cony.row_factory = sqlite3.Row
   
    currr = cony.cursor()
    currr.execute("select * from hostel_records")
   
    rows = currr.fetchall()
    return render_template('display.html',rows = rows)

if __name__ == '__main__':
   app.run(debug = True)

if __name__ == '__main__':
    app.run(debug = True)
