from flask import Flask
app = Flask(__name__)

flag = "Vulntine{ssrf_1s_c00l_bruhh_1234}"
@app.route("/")
def main():
    return "Hi there!"

@app.route("/flag")
def getflag():
    return flag

app.run('0.0.0.0',8100,debug=False)