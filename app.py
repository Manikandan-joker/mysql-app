##import os
from flask import Flask
#from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
app = Flask(__name__)



#mysql = MySQL()

#mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or  'localhost'

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'app'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)
#mysql.init_app(app)

#conn = mysql.connect()

sql = """CREATE TABLE DEMO(
    FIRST_NAME CHAR(20) NOT NULL,
    AGE INT
)"""
sql1 = """INSERT INTO DEMO(
     FIRST_NAME,AGE('Mani',23)
)"""
sql2 = "SELECT * FROM DEMO"

#cursor = connection.cursor()
@app.route("/")
def main():
    return "Welcome!"


@app.route('/msg')
def hello():
    return 'I am good, how about you?'


@app.route('/write')
def write():
    cur = mysql.connection.cursor()
    cur.execute(sql)
    cur.execute(sql1)
    fetchdata= cur.fetchall()
    cur.close()
    return fetchdata




if __name__ == "__main__":
    app.run(debug=True)
