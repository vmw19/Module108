

def test_dict():
    print("Testing dictionaries")

    me ={
        "first_name": "Victoria",
         "last_name": "Warren",
         "age":36,
         "address": {
            "num": 42,
            "street":"evergreen",
            "city": "Springfield",
         }
    }

    #print full name
    print(me["first_name"] + " " + me ["last_name"])

    #modify
    #me["age"] = me["age"] + 1

    #add new keys
    me["color"] = "purple"

    #remove age
    del me["age"]
    # me["age"].pop()

    #print the address
    print(me["address"])

    #street #num, city
    address =  me["address"]
    print(address["street"] + " #" + str(address["num"])+ " ," + {address['city']})


    print(f"{address['street']} #{address['num']}, {address['city']}")

    # last, first
    print(f"{me['last_name']}, {me['first_name']}")

    # Hi my name is _______, _________ and I'm ___years old.
    print(f"Hi my name is {me['first_name']} {me['last_name']}, and I'm {me['age']}years old.")

    #read a key that doesn't exist
    try:
        print(me['xyx'])
    except:
        print("Unexpected error")

    #check if the key exist before reading it
    if "xyz" in me:
        print(me["xyz"])


    print(me)


test_dict()