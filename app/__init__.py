from flask import Flask

app = Flask(__name__)

from config import SECRET_KEY
from flask.ext.mysql import MySQL
import csv

app.secret_key = SECRET_KEY

mysql = MySQL()


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'matviews'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

from app import routes