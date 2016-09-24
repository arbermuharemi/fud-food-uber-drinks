import MySQLdb

host = "localhost"
server_user = "root"
server_password = "hackgt2016"
database = "user_accounts"

db = MySQLdb.connect(host, server_user, server_password, database)

cursor = db.cursor()

def user_auth(username, password):
    is_valid_user = False
    query = "select UserName, Password \
             from users \
             where UserName = username"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        db_user = results[0][0]
        print results
        print db_user
        db_password = results[0][1]
        print password
        if username == db_user and password == db_password:
            is_valid_user = True
        else:
            raise Exception
    except:
        print "Username or password was invalid"
    return is_valid_user
print user_auth("bob", "passo")

