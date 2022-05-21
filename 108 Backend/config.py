import pymongo
import certifi



con_str = "mongodb+srv://vmw19:Heritage23!@cluster0.ashsw.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("ShoeCity")