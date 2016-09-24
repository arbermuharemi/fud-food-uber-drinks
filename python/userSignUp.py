import MySQLdb
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

host = "localhost"
server_user = "root"
server_password = "hackgt2016"
database = "user_accounts"

db = MySQLdb.connect(host, server_user, server_password, database)

cursor = db.cursor()
firstname = ""
lastname = ""

@app.route('/getNames', methods = ['GET', 'POST'])
def getNames():
    firstname = request.form['firstName']
    lastname = request.form['lastName']

@app.route('/checkUserName', methods=['GET', 'POST'])
def checkUserName():
    sql = """select UserName from users;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    isValid = True
    username = request.form['userField']
    password = request.form['passField']

    for row in results:
        for entry in row:
            if (username == entry):
                isValid = False
    if (isValid):
        return redirect(url_for('addUserToDatabase1'), username = username, password = password, firstname = firstname, lastname = lastname)
    else:
        return redirect(url_for('incorrectUser'))

@app.route('/incorrectUser')
def incorrectUser():
    return "This username is taken. Please sign up with another username."

@app.route('/addUserToDatabase1')
def addUserToDatabase1(username, password, firstname, lastname):
    username_insert = '\'' + username + '\''
    password_insert = '\'' + password + '\''
    firstname_insert = '\'' + firstname + '\''
    lastname_insert = '\'' + lastname + '\''
    columnsStatement = 'insert into users (UserName, Password, FirstName, LastName)'
    sql = columnsStatement + 'values(%s, %s, %s, %s)' %(username_insert, password_insert, firstname_insert, lastname_insert)
    cursor.execute(sql)
    db.commit()

def addUserToDatabase2(height, weight, drinks, dietaryRestrictions, food, amountOwed):
    drinks_insert = '\'' + drinks + '\''
    dietaryRestrictions_insert = '\'' + dietaryRestrictions + '\''
    food_insert = '\'' + food + '\''
    height_insert = '\'' + height + '\''
    columnsStatement = 'insert into users (Height, Weight, Drinks, DietaryRestrictions, Food, AmountOwed)'
    sql = columnsStatement + 'values(%s, %d, %s, %s, %s, %d)' %(height_insert, weight, drinks_insert, dietaryRestrictions_insert, food_insert, amountOwed)
    cursor.execute(sql)
    db.commit()

if __name__ == '__main__':
    app.run(debug = True)