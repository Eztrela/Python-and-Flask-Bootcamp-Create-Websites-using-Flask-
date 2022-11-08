import os
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

# Full path of actual directory for this file
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#CREATE DB
db = SQLAlchemy(app)

###############################################################

class Puppy(db.Model):

    # MANUAL TABLHE NAME CHOICE
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        

    def __repr__(self) -> str:
        return f'Puppy {self.name} is {self.age} year/s old'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
 