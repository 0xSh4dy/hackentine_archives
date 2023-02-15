from flask import Flask
app = Flask(__name__)

flag = "Vulntine{fake_flag}" # Real flag is stored on the server

@app.route("/")
def main():
    return "Hi there!"

@app.route("/flag")
def getflag():
    return flag

app.run('0.0.0.0',8100,debug=False)