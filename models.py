from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title',db.String(100), nullable=False)
    description = db.Column('Description', db.String(500), nullable=False)
    date_created = db.Column('Date Created', db.DateTime, default=datetime.datetime.now)
    date_updated = db.Column('Date Updated', db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f'''<Project( Title: {self.title},
        Description: {self.description}, 
        Date Created: {self.date_created}, 
        Date Updated: {self.date_updated} )>'''
    