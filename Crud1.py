from flask import *
import sqlite3

app  = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add")
def add():
    return render_template("add.html")
@app.route("/saveemp",methods=["POST","GET"])

def save():
    if request.method=="POST":
        
        name = request.form["name"]
        email= request.form["email"]
        # print(name, email)
        with sqlite3.connect("employee.db") as con:
            cur = con.cursor()
            cur.execute("Insert into emp(name, email) values(?,?) ",(name,email))
            con.commit()
            print("saved successfully")
        return render_template("index.html")
    

@app.route("/view")

def view():
    con = sqlite3.connect("employee.db")
    con.row_factory = sqlite3.Row
    cur= con.cursor()
    cur.execute("select * from emp")
    rows = cur.fetchall()
    return render_template("view.html",rows=rows)



@app.route("/delete")

def delete():
    return render_template("delete.html")

@app.route("/deleterecord",methods=["POST"])

def deleterecord():
    if request.method=="POST":
        id = request.form["id"]
        with sqlite3.connect("employee.db") as con:
            cur = con.cursor()
            cur.execute("delete from emp where id=?",id)
            con.commit()
            print("deleted successfully")
        return render_template("index.html")

app.run()

