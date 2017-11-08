from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask('chris')


@app.route('/')
@app.route('/<name>')
def hello_chris(name = None):
	return render_template('hello.html',name = name)

app.run(port=8000,debug=True)
logging.info('Server is started at 8000')