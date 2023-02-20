from flask import Flask, render_template, request, make_response, redirect,render_template_string
import random
import string
from hashlib import sha256
import os
import json

app = Flask(__name__)

flag = "Vulntine{burp_suite_ftw_1236437643754}" 

defaultBalance = 70000

def setup():
    with open("db.json","w") as f:
        f.write(json.dumps({"users":[]}))

@app.route("/", methods=["GET", "POST"])
def main():
    username = request.cookies.get("infosec_user")
    if username==None:
        return redirect("/register")
    else:
        if user_exists(username):
            balance = get_balance(username)
            return render_template("index.html",balance=balance)
        else:
            return redirect("/logout")

def user_exists(username):
    f = open("db.json","r")
    users = json.loads(f.read())["users"]
    for user in users:
        if user["username"]==username:
            f.close()
            return True
    f.close()
    return False

@app.route("/register", methods=["GET", "POST"])
def register():
    try:
        data = request.cookies["infosec_user"]
        return redirect("/")
    except Exception as e:
        if request.method == "POST":
            username = request.form["username"]
            resp = make_response(render_template("success.html"))
            resp.set_cookie("infosec_user", username)

            if user_exists(username):
                return resp
            else:
                f = open("db.json","r")
                user_data = json.loads(f.read())
                users = user_data["users"]
                users.append({"username":username,"balance":defaultBalance})
                f.close()
                g = open("db.json","w")
                g.write(json.dumps({"users":users}))
                return resp
        return render_template("register.html")


def get_balance(username):
    f = open("db.json","r")
    users = json.loads(f.read())["users"]
    for user in users:
        if user["username"]==username:
            return user["balance"]
    return 0

def saveBalance(username,balance):
    f = open("db.json","r")
    users = json.loads(f.read())["users"]
    users_write = []
    for user in users:
        if user["username"]==username:
            user["balance"]= balance
        users_write.append(user)
    f.close()
    g = open("db.json","w")
    g.write(json.dumps({"users":users_write}))
    g.close()

@app.route("/buy",methods=["POST"])
def buy():
    try:
        username = request.cookies["infosec_user"]
    except Exception as e:
        return redirect("/register")
    if request.method=="POST":
        data= request.get_json()
        choice = data["choice"]
        price = data["price"]
        balance = get_balance(username)
        if price>balance:
            return "Insufficient funds"
        elif price<balance:
            balance = balance-price
            saveBalance(username,balance)
            if choice=="sin3point14' surprise":
                return f"Good job, this is Sin3point14's surprise ->  {flag}"
            else:
                return f"Purchased one {choice} exploit"



@app.route("/logout",methods=["GET"])
def logout():
    resp = make_response(render_template_string("Logged out"))
    resp.set_cookie("infosec_user",'',expires=0)
    return resp

def main():
    setup()
    app.run("0.0.0.0", 8013, debug=False)

main()
