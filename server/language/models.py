from google.appengine.ext import db

class User(db.Model):
    phoneId = db.StringProperty(required=True)
    firstname = db.StringProperty()
    lastname = db.StringProperty()
    date_created = db.DateProperty()

class Sentence(db.Model):
    value = db.StringProperty(required=True)
    group = db.StringProperty(required=True)
    locale = db.StringProperty(required=True)

class Assessment(db.Model):
    phoneId = db.StringProperty(required=True)
    sentenceId = db.StringProperty(required=True)
    score = db.FloatProperty(required=True, default=-1)
    date_created = db.DateTimeProperty()