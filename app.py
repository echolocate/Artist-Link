from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://mdance@mdmysqlserver:7mWqyn*8Zys2@mdmysqlserver.mysql.database.azure.com:3306/mydatabase'

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

