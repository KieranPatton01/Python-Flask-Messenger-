from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

@app.route("/", methods=['GET','POST'])
def index():
    #if the user submits the log in form...
    if request.method == 'POST':

        connection = sqlite3.connect('var/sqlite3.db')
        cursor = connection.cursor()

        email = request.form['email']
        password = request.form['password']

        query = "SELECT email, password, uid FROM users WHERE email='"+email+"' AND password='"+password+"' "
        cursor.execute(query)
        results = cursor.fetchall()
        #print(results)

        if len(results) == 0:

            print("wrong username/pass")

        else:

            for row in results:
                uid = row[2]

            session["uid"] = uid
            print(uid)
            print("correct user/pass")
            return redirect("http://webtech-45.napier.ac.uk:5000/s", code=302)

    return render_template('login.html')

@app.route("/s")
def test():
    if "uid" in session:
        uid = session["uid"]
        print(uid)
    return uid

if __name__ == "__main__":
    app.run(run)

