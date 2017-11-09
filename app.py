from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
from ormtest import actor,db,app
import logging

#app = Flask('chris')
#应考虑app要在哪里实例化

@app.route('/index')
@app.route('/index/<name>')
def hello_chris(name = None):
	return render_template('hello.html',name = name)

#11.9 methods错写成method
@app.route('/check',methods = ['GET','POST'])
def check():
	if request.method == 'POST':
		actor_id = request.form.get('id',None)
		act = actor.query.filter(actor.actor_id == str(actor_id)).one()
		return render_template('show.html',actor = act)
	else:
		return render_template('check.html')
		#11.9 忘了写return ValueError: View function did not return a response


app.run(port=8000,debug=True)
logging.info('Server is started at 8000')