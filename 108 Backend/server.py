
from flask import Flask 
import json
from mock_data import mock_catalog

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
#######################API CATALOG############################################
@app.route("/api/about", methods=["POST"])  
def about():
    me = {
        "first": "Victoria",
        "last": "Warren"
    }
    return json.dumps(me) # parse into json, then return

@app.route("/api/catalog")  
def get_catalog():
    return  json.dumps(mock_catalog)

#/api/catalog/cheapest
# returns the cheapest product in the catalog
@app.route("/api/catalog/cheapest")
def get_cheapest():
    solution = mock_catalog[0]
    for prod in mock_catalog:
        if prod["price"] <solution ["price"]:
            solution = prod

    return json.dumps(solution)

    #/api/catalog/total
    # return the sume of all product's price

#start the server
app.run(debug=True)

