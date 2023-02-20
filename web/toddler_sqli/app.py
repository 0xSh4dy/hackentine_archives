from flask import Flask,render_template,request,redirect
import sqlite3
import random
import string

app = Flask(__name__)

flag = "Vulntine{ev4d3d_7h0s3_f1l7ers_l1k3_h1s_ex_4v01d3d_h1m}" 


def setup():
    connection = sqlite3.connect("hackentine.db")
    try:
        connection.execute("CREATE TABLE users(username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")
        username = "admin"
        password = ''.join(random.choices(string.ascii_letters,k=32))
        query = f'INSERT INTO users(username,password) VALUES ("{username}","{password}")'
        connection.execute(query)
        connection.commit()
    except sqlite3.OperationalError as err:
        print(err)
    connection.close()

def sanitizeString(data):
    data = str(data).lower()
    data = data.replace("or","")
    data = data.replace("--","")
    return data

@app.route("/",methods=["GET","POST"])
def index():
    connection = sqlite3.connect("hackentine.db")
    cursor = connection.cursor()

    if request.method=="POST":
        username = sanitizeString(request.form["username"])
        password = sanitizeString(request.form["password"])
        query = f"SELECT * FROM users WHERE username='{username}' and password='{password}'"
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            if result!=None:
                return flag
            else:
                return "Try harder"

        except Exception as e:
            return "Error"
    return render_template("index.html")


def run():
    setup()


def main():
    run()
    app.run("0.0.0.0",8013,debug=False)

main()