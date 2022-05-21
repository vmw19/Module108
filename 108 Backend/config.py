import pymongo
import certify


con_str = "mongodb+srv://vmw19:Heritage23!@cluster0.ashsw.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certify.where())

db = client.get_database("ShoeCity")