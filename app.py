from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://152.58.155.221:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    name = data.get('name')
    password = data.get('password')
    gender = data.get('gender')
    size = data.get('size')
    typ = data.get('type')
    age = data.get('age')
    gender_pref = data.get('gender_preference')
    
    user_data = {
        "name": name,
        "password": password,
        "gender": gender,
        "size": size,
        "type": typ,
        "age": age,
        "gender_preference": gender_pref
    }
    print(user_data)
    mycol.insert_one(user_data)

    return jsonify({
        "status": "success",
        "message": "Login data inserted successfully",
        "data": user_data
    })
    
app.run()
