from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:940425@localhost:3306/test?charset=utf8'
#11.8 理解"数据库驱动" 默认MySQLdb在python 3已不支持 需手动改为mysqlconnector或pymysql
db = SQLAlchemy(app)

class actor(db.Model):
	__tablename__ = 'actor'

	actor_id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20))
	last_name = db.Column(db.String(20))
	last_update = db.Column(db.String(20))

	def __init__(self, actor_id, first_name, last_name, last_update):
		self.actor_id = actor_id
		self.first_name = first_name
		self.last_name = last_name
		self.last_update = last_update

	def __repr__(self):
		return 'Actor_id:{} \nFirst_name:{} \nLast_name:{} \nLast_update:{}'.format(self.actor_id,self.first_name,self.last_name,self.last_update)

#act = actor.query.filter(actor.actor_id == '4').one()
#print(act)