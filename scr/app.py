from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from marshmallow import Schema, fields, validate, ValidationError
app = Flask(__name__)

client = MongoClient('db', 27017)
db = client.flask_db

class MyValidSchema(Schema):
    id = fields.Integer()
    string = fields.String()
@app.route('/', methods=['GET', 'POST'])
def get():

    results = db.flask_db.find()

    return render_template('flask_app.html', results=results), 200

@app.route('/post', methods=['POST'])
def post():

    id = (request.form['id'])
    string = request.form['string']

    error = MyValidSchema().validate({"id": id, "string": string})
    if error:
        raise ValidationError("Wrong input")

    item_doc = {
        'id': id,
        'string': string
    }

    db.flask_db.insert_one(item_doc)
    return redirect(url_for("get")), 300

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)