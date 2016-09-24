import MySQLdb

host = "localhost"
user = "root"
password = "hackgt2016"
database = "user_accounts"

db = MySQLdb.connect(host, user, password, database)

cursor = db.cursor()

def user_auth(username, password):
    query = "select UserName, Password \
             from users \
             where UserName = username"
    is_valid_user = False
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        user = results[0][0]
        print user
        password = results[0][1]
        print password
    except:
        print "Username or password was invalid"
    return is_valid_user

print user_auth("user", "password")
