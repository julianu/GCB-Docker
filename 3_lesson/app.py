import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb

@app.route('/')
def todo():
  _items = db.tododb.find()
  items = [item for item in _items]
  return render_template('todo.html', items=items)

@app.route('/new', methods=['POST'])
def new():
  content = request.get_json(force=True)
  item_doc = {
      'name': content['name'],
      'description': content['description']
  }
  db.tododb.insert_one(item_doc)

  return todo()

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
