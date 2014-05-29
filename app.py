import logging      
from logging import FileHandler
from flask import Flask
from views import site_index
from views import app
from flask.ext.sqlalchemy import SQLAlchemy

file_handler = FileHandler("debug.log","a")                                                                                             
file_handler.setLevel(logging.WARNING)

app.logger.addHandler(file_handler)
app.register_blueprint(site_index)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

if app.config['DEBUG']:
    from werkzeug import SharedDataMiddleware
    import os
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
      '/': os.path.join(os.path.dirname(__file__), 'static')
    })
