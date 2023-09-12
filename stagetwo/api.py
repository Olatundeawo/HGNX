#!/usr/bin/env python3
"""Flask app
"""
import sys
import os
from flask import Flask, Response, request, jsonify, render_template
from typing import Dict
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import json
from dataclasses import dataclass

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@dataclass
class Person(db.Model):
    """Define a table for a person """
    id: int
    name: str
    
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        """String representation"""
        return ('The name you save is {}'.format(self.name))
    

@app.route('/api', methods=['GET', 'POST'])
def create_name():
    """Method for adding a new name to the database"""
    if request.method == 'POST':
        name_input = sys.argv[1]
        person = Person(name=name_input)
        db.session.add(person)
        db.session.commit()
        return (jsonify({"Message": "Name successfully added"}))
    return ("Page for adding a name")
        

# Used to fetch all items
@app.route('/get', methods=['GET'])
def get_all_items():
    """Get all items
    """
    all_name = Person.query.all()
    return (jsonify(all_name))


# Reading data
@app.route('/api/<int:user_id>', methods=['GET'])
def get_items(user_id):
     """Method that fetch data"""
     name = Person.query.get(user_id)
     if name is None:
         return (jsonify({"Message":"Name not in list"}), 404)
     return jsonify(name)
 
# Update an existing name
@app.route('/api/<int:user_id>', methods=['PUT'])
def update_item(user_id):
    """Method that change name with a
    particular id"""
    names = Person.query.get_or_404(user_id)
    if request.methods == "PUT":
        new_name = sys.argv[2]
        
        names.name = new_name
        
        db.session.add(names)
        db.session.commit()
        return (jsonify({"Message": "Name successfully deleted"}))

# Delete a name
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_item(user_id):
    """Method to delete a name based on an item"""
    names = Person.query.get_or_404(user_id)
    if request.method == "DELETE":
        db.session.delete(names)
        db.session.commit()
        return (jsonify({"Message": "Name successfully deleted"}))

if __name__ == "_main__":
    db.create_all()
    app.run(debug=True)