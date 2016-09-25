import MySQLdb

host = "localhost"
server_user = "root"
server_password = "hackgt2016"
database = "user_accounts"

db = MySQLdb.connect(host, server_user, server_password, database)

cursor = db.cursor()


def purchaseFood(food_item, quantity):
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
        return False
    new_quantity = db_quantity - quantity
    sqlpost = "update food set Quantity = %d where FoodName = %s" % (new_quantity, food_item_insert)
    cursor.execute(sqlpost)
    db.commit()
    return True

def foodcalorieCount(food_item, quantity):
    food_item_insert = '\'' + food_item + '\''
    sql = "select Calories from Food where FoodName = %s" % food_item_insert
    cursor.execute(sql)
    results = cursor.fetchall()
    caloriesPerItem = int(results[0][0])
    return caloriesPerItem * quantity

def foodamountDue(username, food_item, quantity):
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
    totalAmountOwed = totalPrice + float(results[0][0])
    usersqlpost = "update users set AmountOwed = %f where UserName = %s" % (totalAmountOwed, username_insert)
    cursor.execute(usersqlpost)
    db.commit()
    return totalPrice

def purchaseDrink(drink_item, quantity):
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
        return False
    new_quantity = db_quantity - quantity
    sqlpost = "update drink set Quantity = %d where DrinkName = %s" % (new_quantity, drink_item_insert)
    cursor.execute(sqlpost)
    db.commit()
    return True

def drinkcalorieCount(drink_item, quantity):
    drink_item_insert = '\'' + drink_item + '\''
    sql = "select Calories from drink where DrinkName = %s" % drink_item_insert
    cursor.execute(sql)
    results = cursor.fetchall()
    caloriesPerItem = int(results[0][0])
    return caloriesPerItem * quantity

def drinkamountDue(username, drink_item, quantity):
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
    totalAmountOwed = totalPrice + float(results[0][0])
    usersqlpost = "update users set AmountOwed = %f where UserName = %s" % (totalAmountOwed, username_insert)
    cursor.execute(usersqlpost)
    db.commit()
    return totalPrice