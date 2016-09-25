import MySQLdb
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

host = "localhost"
server_user = "root"
server_password = "hackgt2016"
database = "user_accounts"

db = MySQLdb.connect(host, server_user, server_password, database)

cursor = db.cursor()
currentUser = ""
flightCode = ""
dateOfDeparture = ""

@app.route('/authenticate', methods = ['GET', 'POST'])
def user_auth():
    original_user = request.form['userField']
    original_pass = request.form['passField']
    username = '\'' + original_user + '\''
    password = '\'' + original_pass + '\''
    is_valid_user = False
    query = "select UserName, Password \
             from users \
             where UserName = " + username
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        db_user = results[0][0]
        db_password = results[0][1]
        if original_user == db_user and original_pass == db_password:
            is_valid_user = True
        else:
            raise Exception
    except:
        return redirect(url_for('incorrectLogin'))
    currentUser = username
    return render_template('FlightNumber.html')

@app.route('/incorrectLogin')
def incorrectLogin():
    return 'Your Login information was incorrect. Please try again'

@app.route('/checkUserName', methods=['GET', 'POST'])
def checkUserName():
    sql = """select UserName from users;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    isValid = True
    user = request.form['userField']
    myPass = request.form['passField']
    first = request.form['firstName']
    last = request.form['lastName']
    for row in results:
        for entry in row:
            if (user == entry):
                isValid = False
    if (isValid):
        return redirect(url_for('addUserToDatabase1', username = user, password = myPass, firstname = first, lastname = last))
    else:
        return redirect(url_for('incorrectUser'))

@app.route('/incorrectUser')
def incorrectUser():
    return "This username is taken. Please sign up with another username."

@app.route('/addUserToDatabase1/<username>/<password>/<firstname>/<lastname>')
def addUserToDatabase1(username, password, firstname, lastname):
    username_insert = '\'' + username + '\''
    password_insert = '\'' + password + '\''
    firstname_insert = '\'' + firstname + '\''
    lastname_insert = '\'' + lastname + '\''
    columnsStatement = 'insert into users (UserName, Password, FirstName, LastName)'
    sql = columnsStatement + 'values(%s, %s, %s, %s)' %(username_insert, password_insert, firstname_insert, lastname_insert)
    cursor.execute(sql)
    db.commit()
    return render_template('UserReg2.html')

@app.route('/addUserToDatabase2', methods = ['GET', 'POST'])
def addUserToDatabase2():
    height = request.form['heightField']
    weight = int(request.form['weightField'])
    drinks = request.form['drinkSelect']
    dietaryRestrictions = request.form.getlist('restrictionSelect');
    dietaryRestrictions = ','.join(dietaryRestrictions)
    food = request.form['foodSelect']
    amountOwed = 0
    drinks_insert = '\'' + drinks + '\''
    dietaryRestrictions_insert = '\'' + dietaryRestrictions + '\''
    food_insert = '\'' + food + '\''
    height_insert = '\'' + height + '\''
    columnsStatement = 'insert into users (Height, Weight, Drinks, DietaryRestrictions, Food, AmountOwed)'
    sql = columnsStatement + 'values(%s, %d, %s, %s, %s, %d)' %(height_insert, weight, drinks_insert, dietaryRestrictions_insert, food_insert, amountOwed)
    cursor.execute(sql)
    db.commit()
    return render_template('FlightNumber.html')

@app.route('/storeFlightInfo', methods = ['GET', 'POST'])
def storeFlightInfo():
    flightCode = request.form['flightField']
    dateOfDeparture = request.form['dateField']
    sql = 'insert into users (FlightCode, Date) values(%s, %s) where UserName = %s' % (flightCode, dateOfDeparture, currentUser)
    cursor.execute(sql)
    db.commit()
    return render_template('Application.html')

@app.route('/toWelcomePage', methods = ['GET', 'POST'])
def toWelcomePage():
    return render_template('index.html')

@app.route('/toLoginPage', methods = ['GET', 'POST'])
def toLoginPage():
    return render_template('Login.html')

@app.route('/toUserRegistration', methods = ['GET', 'POST'])
def toUserRegistration():
    return render_template('UserReg.html')

if __name__ == '__main__':
    app.run(debug = True)