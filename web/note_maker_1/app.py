from flask import Flask, render_template, request, make_response, redirect,render_template_string
import random
import string
from hashlib import sha256
import os

notes_store = "notes/"
app = Flask(__name__)
os.system("mkdir notes")

def generate_random_string(str_length):
    rand_str = random.choices(string.ascii_lowercase, k=str_length)
    return ''.join(rand_str)


def get_notes(username):
    notes = os.listdir(notes_store)
    user_notes = []
    for note in notes:
        if username in note:
            user_notes.append(note)
    return user_notes

@app.route("/", methods=["GET", "POST"])
def main():
    username = request.cookies.get("note_user")
    if username==None:
        return redirect("/register")
    if request.method == "POST":
        user_note = request.form["note"]
        note_store = username + "_"+generate_random_string(16)
        note_store = "notes/"+note_store+".txt"
        print("POST")
        with open(note_store, "w") as note_file:
            note_file.write(user_note)
        return render_template("success.html")
    
    else:
        user_notes = get_notes(username)
        return render_template("index.html",notes=user_notes)



@app.route("/register", methods=["GET", "POST"])
def register():
    try:
        data = request.cookies["note_user"]
        return redirect("/")
    except Exception as e:
        if request.method == "POST":
            username = request.form["username"]
            resp = make_response(render_template("success.html"))
            resp.set_cookie("note_user", username)
            return resp
        return render_template("register.html")


@app.route("/notes",methods=["GET"])
def render_note():
    file = request.args["file"]
    f = open(notes_store+file,"r")
    data = f.read()
    return data

@app.route("/logout",methods=["GET"])
def logout():
    resp = make_response(render_template_string("Logged out"))
    resp.set_cookie("note_user",'',expires=0)
    return resp

app.run("0.0.0.0", 8007, debug=False)
