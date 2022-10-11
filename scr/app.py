from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('db', 27017)
db = client.flask_db

@app.route('/')
def todo():

    _items = db.flask_db.find()
    items = [item for item in _items]

    return render_template('flask_app.html', items=items)

@app.route('/post', methods=['POST'])
def post():

    item_doc = {
        'id': request.form['id'],
        'string': request.form['string']
    }
    db.flask_db.insert_one(item_doc)

    return redirect(url_for("todo"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)