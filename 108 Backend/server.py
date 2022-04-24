
from flask import Flask 

app =  Flask('server')

@app.route("/home")
def home():
    return "Hello there!"

@app.route("/")
def home():
    return "Welcome to the online store server"

@app.route("/about")
def about_me():
    return "My name is Victoria"

#start the server
app.run(debug=True)

