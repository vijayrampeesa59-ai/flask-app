from flask import app, render_template,request,Flask
from pymongo import MongoClient

# MongoDB Atlas connection
MONGO_URI = "mongodb+srv://dummy:1234@tram.uzwi1fl.mongodb.net/?appName=tram"
mongo_client = MongoClient(MONGO_URI)
db = mongo_client['Flask']
mongo = db['Data']

@app.route('/todo') 
def todo(): 
    return render_template('todo.html')


@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    item_name = request.form['itemName']
    item_desc = request.form['itemDescription']
    todo_item = {"itemName": item_name, "itemDescription": item_desc}
    mongo.db.todos.insert_one(todo_item)
    return "Item added to DB!", 201