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
                isValid = False
    return isValid

def addUserToDatabase(username, password, firstname, lastname, height, weight, drinks, dietaryRestrictions, food, amountOwed):
    username_insert = '\'' + username + '\''
    password_insert = '\'' + password + '\''
    firstname_insert = '\'' + firstname + '\''
    lastname_insert = '\'' + lastname + '\''
    drinks_insert = '\'' + drinks + '\''
    dietaryRestrictions_insert = '\'' + dietaryRestrictions + '\''
    food_insert = '\'' + food + '\''
    height_insert = '\'' + height + '\''
    sql = """insert into users (UserName, Password, FirstName, LastName, Height, Weight, Drinks, DietaryRestrictions, Food, AmountOwed)
    values(""" + username_insert + ',' + password_insert + ',' +  firstname_insert + ',' + lastname_insert + ',' + height + ',' + weight + ',' + drinks_insert + ',' + dietaryRestrictions_insert + ',' + food_insert + ',' + amountOwed + """)"""
    cursor.execute(sql)

addUserToDatabase('jbutler', 'frontend', 'Jacob', 'Butler', '5 feet 11 inches', 190, 'Ginger Ale', 'Not Applicable', 'Sandwiches', 0)
print (checkUserName("amuharemi"))