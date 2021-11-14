from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://mdance@mdmysqlserver:7mWqyn*8Zys2@mdmysqlserver.mysql.database.azure.com:3306/mydatabase'

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)