from flask import Flask,render_template,render_template_string,request
import random

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])

def main():
    colors = ["blue","pink","chartreuse","skyblue","red","orange","green","darkred","cyan"]
    if request.method=="GET":
        return render_template("index.html")
    elif request.method=="POST":
        rand_color = random.choices(colors)[0]
        name = request.form['sweetheart']
        return render_template_string(f"<span style='font-size:20px'>Your sweetheart -> </span><span style='color:{rand_color};font-size:30px'>{name}</span>")

app.run("0.0.0.0",8002,debug=False)