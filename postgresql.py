import psycopg2
import json
import konfig

class PostgreSQL:
	def __init__(self):
		self.connectionString = "dbname='"+konfig.dbName+"' user='"+konfig.dbUsername+"' host='"+konfig.dbHost+"' password='"+konfig.dbPassword+"'";
	
	def alternativeInit(self,_dbname,_username,_password,_host):
		self.dbname = _dbname
		self.username = _username
		self.password = _password
		self.host = _host
		self.connectionString = "dbname='"+self.dbname+"' user='"+self.username+"' host='"+self.host+"' password='"+self.password+"'";

	def executeQuery(_query):
		try:
			conn = psycopg2.connect(self.connectionString)
			cur = conn.cursor()
			cur.execute(_query)
			rows = cur.fetchall()
			return str(json.dumps(rows))
		except:
			print "Cant Connect To DB, DBGG"

