from flask import Flask
from views import app
from app import db

class Entry(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(150))
	content = db.Column(db.String(1500))
	
	def __init__(self, title, content):
		self.title = title
		self.content = content
