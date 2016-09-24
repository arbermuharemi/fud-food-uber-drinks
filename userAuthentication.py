import MySQLdb

host = "localhost"
user = "root"
password = ""
database = "user_accounts"

db = MySQLdb.connect(host, user, password, database)

cursor = db.cursor()

