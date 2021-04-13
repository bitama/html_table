from flask import Flask,render_template,redirect
from base import users

users = users()

app = Flask(__name__)

@app.route("/")
def index():
    print(users)
    return render_template("index.html",users = users)



if __name__=="__main__":
    app.run(debug=True)