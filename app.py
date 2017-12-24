from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import main

app = Flask(__name__)
app.config['DEBUG'] = True #displays runtime errors in the browser
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://golfapp:golfapp@localhost:8889/golfapp'
#mysqldump -h localhost:8889 -u golfapp -pgolfapp golfapp > backup.sql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://cqx01uvb2wce9v5y:kus9g2j2437c835u@tk3mehkfmmrhjg0b.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/ypgr5fx3g3icm84n'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
