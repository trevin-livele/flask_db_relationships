import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #pip install Flask-Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)




class Puppy(db.Model):


    __tablename__ = 'puppies'

    id = db.column(db.Integer,primary_key=True)
    name = db.column(db.Text)
    #one to many
    #puppy to many toys
    toys = db.relationship('Toy',backref='puppy',lazy='dynamic')
    #one to one 
    #one puppy to one owner
    Owner = db.relationship('Owner',backref='puppy',uselist=False)


    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and no owner yet!"

    def report_toys(self):
        print("Here are my toys")
        for toy in self.toys:
            print(toy.item_name)
        



class Toy(db.Model):
    

    __tablename__ = 'toys'

    id = db.Column(db.integer,primary_key=True)
    item_name = db.Columns(db.Text)
    puppy_id = db.column(db.Integer,db.ForeignKey('puppies.id'))


    def __init__(self,item_name,puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id

class Owner(db.Model):


    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)


    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))


    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id



#export FLASK_APP=basic.py
#flask db init
#flask db migrate -m "created pupppy table"
#flask db upgrade
