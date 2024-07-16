'''
USE:
$env:FLASK_APP = "api.py"
flask run

then you can use:
yarn start

'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(os.getcwd(), "tasks.db")
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f'{self.id} {self.content}'

@app.route('/api', methods=['GET'])
def index():
    return {
        'name': ['apple, orange']
    }

if __name__ == '__main__':
    app.run(debug=True)