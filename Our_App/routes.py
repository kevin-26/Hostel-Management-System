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
@app.route('/about')
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
        with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO records (room_no,name,roll_no,age,gender,branch)VALUES (?,?,?,?,?,?)",(302,nm,2,age,gender,branch) )
                
                con.commit()
    except:
        con.rollback()
      
      
    finally:
        return "done"
        con.close()

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
