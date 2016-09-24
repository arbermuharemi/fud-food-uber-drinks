import MySQLdb

host = "localhost"
server_user = "root"
server_password = "hackgt2016"
database = "user_accounts"

db = MySQLdb.connect(host, server_user, server_password, database)

cursor = db.cursor()

def checkUserName(username):
    sql = """select UserName from users;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    isValid = True

    for row in results:
        for entry in row:
            if (username == entry):
                isValid = False;
    return isValid

print (checkUserName("amuharemi"))