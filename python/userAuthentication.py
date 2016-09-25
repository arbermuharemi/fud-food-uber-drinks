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
    global currentUser
    original_user = request.form['userField']
    original_pass = request.form['passField']
    print original_user
    print original_pass
    username = '\'' + original_user + '\''
    password = '\'' + original_pass + '\''
    print username
    print password
    is_valid_user = False
    query = "select UserName, Password \
             from users \
             where UserName = " + username
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        db_user = results[0][0]
        print results
        print db_user
        db_password = results[0][1]
        print db_password
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
    global currentUser
    username_insert = '\'' + username + '\''
    password_insert = '\'' + password + '\''
    firstname_insert = '\'' + firstname + '\''
    lastname_insert = '\'' + lastname + '\''
    columnsStatement = 'insert into users (UserName, Password, FirstName, LastName)'
    sql = columnsStatement + 'values(%s, %s, %s, %s)' %(username_insert, password_insert, firstname_insert, lastname_insert)
    cursor.execute(sql)
    db.commit()
    currentUser = username_insert
    return render_template('UserReg2.html')

@app.route('/addUserToDatabase2', methods = ['GET', 'POST'])
def addUserToDatabase2():
    global currentUser
    height = request.form['heightField']
    weight = int(request.form['weightField'])
    drinks = request.form['drinkSelect']
    dietaryRestrictions = request.form.getlist('restrictionSelect');
    dietaryRestrictions = ','.join(dietaryRestrictions)
    print (dietaryRestrictions)
    food = request.form['foodSelect']
    amountOwed = 0
    drinks_insert = '\'' + drinks + '\''
    dietaryRestrictions_insert = '\'' + dietaryRestrictions + '\''
    food_insert = '\'' + food + '\''
    height_insert = '\'' + height + '\''
    columnsStatement = 'update users set Height = %s, Weight = %d, Drinks = %s, DietaryRestrictions = %s, Food = %s, AmountOwed = %f' %(height_insert, weight, drinks_insert, dietaryRestrictions_insert, food_insert, amountOwed)
    sql = columnsStatement + 'where UserName = %s' %(currentUser)
    cursor.execute(sql)
    db.commit()
    return render_template('FlightNumber.html')

@app.route('/storeFlightInfo', methods = ['GET', 'POST'])
def storeFlightInfo():
    global currentUser
    flightCode = '\'' + request.form['flightField'] + '\''
    dateOfDeparture = '\'' + request.form['dateField'] + '\''
    print ("This is start info test " + currentUser + " " + flightCode)
    sql = 'update users set FlightCode = %s where UserName = %s;' %(flightCode, currentUser)
    cursor.execute(sql)
    db.commit()
    return render_template('Application.html')

@app.route('/toWelcomePage', methods = ['GET', 'POST'])
def toWelcomePage():
    global currentUser
    currentUser = ""
    return render_template('index.html')

@app.route('/toLoginPage', methods = ['GET', 'POST'])
def toLoginPage():
    return render_template('Login.html')

@app.route('/toUserRegistration', methods = ['GET', 'POST'])
def toUserRegistration():
    return render_template('UserReg.html')

@app.route('/purchaseFood', methods = ['GET', 'POST'])
def purchaseFood():
    food_item = request.form.get('foodChoices')
    quantity = 1
    food_item_insert = '\'' + food_item + '\''
    sqlget = "select Quantity from food where FoodName = %s" %food_item_insert
    cursor.execute(sqlget)
    results = cursor.fetchall()
    db_quantity = int(results[0][0])
    try:
        if (quantity > db_quantity):
            raise Exception
    except:
        print ("You ordered more than what was available")
    new_quantity = db_quantity - quantity
    sqlpost = "update food set Quantity = %d where FoodName = %s" % (new_quantity, food_item_insert)
    cursor.execute(sqlpost)
    db.commit()
    return redirect(url_for('foodamountDue', food_item = food_item, quantity = quantity))

@app.route('/foodAmountDue/<food_item>/<quantity>', methods = ['GET', 'POST'])
def foodamountDue(food_item, quantity):
    global currentUser
    username = currentUser
    food_item_insert = '\'' + food_item + '\''
    username_insert = '\'' + username + '\''
    foodsql = "select Price from Food where FoodName = %s" % food_item_insert
    cursor.execute(foodsql)
    results = cursor.fetchall()
    pricePerItem = float(results[0][0])
    totalPrice = pricePerItem * quantity
    usersqlget = "select AmountOwed from users where UserName = %s" % username_insert
    cursor.execute(usersqlget)
    results = cursor.fetchall()
    print (results)
    totalAmountOwed = totalPrice + float(results[0][0])
    usersqlpost = "update users set AmountOwed = %f where UserName = %s" % (totalAmountOwed, username_insert)
    cursor.execute(usersqlpost)
    db.commit()
    return render_template('Drink.html')

@app.route('/toUberPage', methods = ['GET', 'POST'])
def toUberPage():
    return render_template("Uber.html")

@app.route('/toDrinkPage', methods = ['GET', 'POST'])
def toDrinkPage():
    return render_template("Drink.html")

@app.route('/toUpdatePage', methods = ['GET', 'POST'])
def toUpdatePage():
    return render_template("UpdatePref.html")

@app.route('/toApplicationPage', methods = ['GET', 'POST'])
def toApplicationPage():
    return render_template("Application.html")

@app.route('/purchaseDrink', methods = ['GET', 'POST'])
def purchaseDrink(drink_item, quantity):
    drink_item = request.form.get('foodChoices')
    quantity = 1;
    drink_item_insert = '\'' + drink_item + '\''
    sqlget = "select Quantity from drink where DrinkName = %s" %drink_item_insert
    cursor.execute(sqlget)
    results = cursor.fetchall()
    db_quantity = int(results[0][0])
    try:
        if (quantity > db_quantity):
            raise Exception
    except:
        print ("You ordered more than what was available")
    new_quantity = db_quantity - quantity
    sqlpost = "update drink set Quantity = %d where DrinkName = %s" % (new_quantity, drink_item_insert)
    cursor.execute(sqlpost)
    db.commit()
    return redirect(url_for('drinkAmountDue', drink_item = drink_item, quantity = quantity))

@app.route('/drinkAmountDue/<drink_item>/<quantity>', methods = ['GET', 'POST'])
def drinkamountDue(drink_item, quantity):
    global currentUser
    username = currentUser
    drink_item_insert = '\'' + drink_item + '\''
    username_insert = '\'' + username + '\''
    foodsql = "select Price from drink where DrinkName = %s" % drink_item_insert
    cursor.execute(foodsql)
    results = cursor.fetchall()
    pricePerItem = float(results[0][0])
    totalPrice = pricePerItem * quantity
    usersqlget = "select AmountOwed from users where UserName = %s" % username_insert
    cursor.execute(usersqlget)
    results = cursor.fetchall()
    print (results)
    totalAmountOwed = totalPrice + float(results[0][0])
    usersqlpost = "update users set AmountOwed = %f where UserName = %s" % (totalAmountOwed, username_insert)
    cursor.execute(usersqlpost)
    db.commit()
    return render_template("Application.html")



if __name__ == '__main__':
    app.run(debug = True)