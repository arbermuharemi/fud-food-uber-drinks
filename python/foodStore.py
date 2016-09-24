import MySQLdb

host = "localhost"
server_user = "root"
server_password = "hackgt2016"
database = "user_accounts"

db = MySQLdb.connect(host, server_user, server_password, database)

cursor = db.cursor()


def purchase_food(food_item, quantity):
    food_item = '\'' + food_item + '\''
    query = "select Quantity, Calories, Price \
             from food \
             where FoodName = " + food_item
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        db_quantity = results[0]
        db_calories = results[1]
        db_price = results[2]
        if quantity > db_quantity:
            raise Exception
    except:
        "Sorry, we only have %d of that item! Please change your order" % (
            db_quantity)




