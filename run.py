from app import app
import logging      
from logging import FileHandler
from flask import Flask
from views import site_index

if __name__ == '__main__':
	app.run(port=8023, use_reloader=True)
	app.debug = True
