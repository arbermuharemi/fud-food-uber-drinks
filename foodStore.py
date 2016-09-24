import MySQLdb

host = "localhost"
server_user = "root"
server_password = "hackgt2016"
database = "user_accounts"

db = MySQLdb.connect(host, server_user, server_password, database)

cursor = db.cursor()


def purchase_food(food_item, quantity):
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

def calorieCount(food_item, quantity):
    food_item_insert = '\'' + food_item + '\''
    sql = "select Calories from Food where FoodName = %s" % food_item_insert
    cursor.execute(sql)
    results = cursor.fetchall()
    caloriesPerItem = int(results[0][0])
    return caloriesPerItem * quantity

def amountDue(username, food_item, quantity):
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
    return totalPrice