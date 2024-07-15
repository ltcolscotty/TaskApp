'''
USE:
$env:FLASK_APP = "api.py"
flask run

then you can use:
yarn start

'''

from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return {
        'name': ['apple, orange']
    }

if __name__ == '__main__':
    app.run(debug=True)