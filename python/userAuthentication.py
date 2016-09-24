import MySQLdb
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

host = "localhost"
server_user = "root"
server_password = "hackgt2016"
database = "user_accounts"

db = MySQLdb.connect(host, server_user, server_password, database)

cursor = db.cursor()

@app.route('/authenticate', methods = ['GET', 'POST'])
def user_auth():
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
    return render_template('Application.html')

@app.route('/incorrectLogin')
def incorrectLogin():
    return 'Your Login information was incorrect. Please try again'

if __name__ == '__main__':
    app.run(debug = True)