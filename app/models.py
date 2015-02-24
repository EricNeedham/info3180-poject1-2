from . import db
from marshmallow import schema 

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fisrt_name = db.Column(db.String(80))
  last_name = db.Column(db.String(80))
  age = db.Column(db.Integer)
  image = db.Column(db.String(120))
  
  def __init__(self, fisrt_name, last_name, age, sex, image):
    self.fisrt_name = fisrt_name
    self.last_name = last_name
    self.age = age
    self.image = image
    
  def __repr__(self):
    return '<User %r>' % self.fisrt_name
class UserSchema(schema):
  formatted_name = fields.Method("format_name")
  
class Meta:
  fields = ('fisrt_name','last_name','age','image')
