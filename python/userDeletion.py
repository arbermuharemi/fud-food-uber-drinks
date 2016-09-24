import MySQLdb

host = "localhost"
server_user = "root"
server_password = "hackgt2016"
database = "user_accounts"

db = MySQLdb.connect(host, server_user, server_password, database)

cursor = db.cursor()

def deleteUser(username):
    username_insert = '\'' + username + '\''
    sql = "delete from users where UserName = %s" % username_insert
    cursor.execute(sql)
    db.commit()
deleteUser('jbutler')