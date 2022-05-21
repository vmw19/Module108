
from flask import Flask, request, abort 
import json
from mock_data import mock_catalog
from config import db
from bson import ObjectId

app =  Flask('server')


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
    cursor = db.products.find({}) # get all
    all_products = []

    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        all_products.append(prod)

        return json.dumps(all_products)
    

@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()
    db.products.insert_one(product)

    print("Product saved!")
    print(product)

    product["_id"] = str(product["_id"])

    return json.dumps(product)

#/api/catalog/cheapest
# returns the cheapest product in the catalog
@app.route("/api/catalog/cheapest")
def get_cheapest():
    solution = mock_catalog[0]
    for prod in mock_catalog:
        if prod["price"] <solution ["price"]:
            solution = prod

    solution["_id"] = str(solution["_id"])
    return json.dumps(solution)

#/api/catalog/total
# return the sume of all product's price
@app.route("/api/catalog/total")
def get_total():
    total = 0
    for prod in mock_catalog:
        total += prod["price"]

        return json.dumps(total)

#find a product based on the unique id
@app.route("/api/product/<id>")
def find_product(id):
    prod = db.products.find_one({"_id": ObjectId(id) })
    prod["id"] = str(prod["_id"])

    return json.dumps(prod)

#get the list of categories from the catalog
#/api/products/categories
#expectes: a list of strings containing the unique prods categories
@app.route("/api/product/categories")
def get_categories():
    categories = []
    cursor = db.products.find({})
    #push all the categories into the list
    for prod in cursor:
        cat = prod["category"]
        if not cat in categories:
            categories.append(cat)

    return json.dumps(categories)

#get all the products that belong to a specified category
#/api/products/categories/heels
@app.route("/api/product/category/<cat_name>")
def get_by_category(cat_name):
    results = []
    cursor = db.products.find({"category": cat_name})
# get the products from the cursor, fix the _id, put them on results
    for prod in cursor:
        prod["id"] = str(prod["_id"])
        results.append

    #add products whose category is equal to name
    for prod in mock_catalog:
        if prod["category"].lower() == cat_name.lower():
            results.append(prod)

    return json.dumps(results)

#search by text inside the title
#receive a text
#return all product whose title contains the text
@app.route("/api/products/search/<text>")
def search_by_text(text):
    results = []

#search and add
    for prod in mock_catalog:
        title = prod["title"].lower()
        if text.lower() in title:
            results.append(prod)

    return json.dumps(results)


#start the server
app.run(debug=True)

##################################################### Coupon Codes ################# _id, code, discount############################################
# 1 - get /api/couponCodes
@app.get("/api/couponCodes")
def get_coupon_codes():
    cursor = db.couponCodes.find({})
    results = []
    for coupon in cursor:
        coupon["_id"]= str(coupon["_id"])
        results.append(coupon)

    return json.dumps(results)

# #2 - get /api/couponCodes/<code>
@app.get("/api/couponCodes/<code>")
def get_by_code(code):
    coupon = db.couponCodes.find_one{{"code":code})
    if not coupon:
        return abort (400, "Invalid coupon code")

    coupon["_id"]= str(coupon["_id"])

    return json.dumps(coupon)

# #3 - POST /api/couponCodes

@app.post("/api/couponCodes")
def save_coupon():
    coupon = request.get_json()

#validate that code exists and contains at least 5 chars
    if not "code" in coupon or len(coupon["code"]) < 5:
     return abort(400, "Code is required and should contain at least 5 chars.")

#validate that code is not over 31%
    if not "discount" in coupon or type(coupon["discount"]) is not type(int) or type(coupon)["discount"]: != type(float):
        return abort(400, "Discount is required and should be a valid number.")

    if not ["discount"] < 0 or coupon ["discount"] > 31:
        return abort(400, "Discount is required and should be between 0 and 31.")

    db.couponCoupon.insert_one(coupon)
    coupon["_id"]= str(coupon["_id"])

    return json.dumps(coupon)

app.run(debug=True)
