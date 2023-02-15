from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def main():
    if request.method=="POST":
        url = request.form["url"]
        response = requests.get(url).text
        return response
    return render_template("index.html")

app.run('0.0.0.0',8010,debug=False)