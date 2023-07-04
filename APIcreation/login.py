from flask import Flask,render_template,request
from flask_restful import Api
from sql import get_sql_conn,get_users_conn
app = Flask(__name__,template_folder='template')

@app.route('/')
def page():
    return render_template("home.html")

@app.route('/login/signup.html',methods=['GET'])
def signuppage():
    return render_template("signup.html")

@app.route('/login/signup',methods=['GET', 'POST'])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    password1 = request.form.get("password1")
    if request.method == "POST":
        cursor = con.cursor()
        if (username.isalnum() and 6 <= len(username) <= 12) and (password == password1) and len(password) > 6:
            query = "INSERT INTO user_info (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, password))
            con.commit()
            data={
            "message":"Data inserted"
            }
            return render_template("signup.html",data=data)
        else:
            data={
                    "message":"username should be alphanumeric and to be between 6-12 letters"
                }
            if not username.isalnum() or not 6 <= len(username) <= 12:
                return render_template("signup.html",data=data)
            elif password != password1:
                data["message"] = "password is not matching with re-enter password"
                return render_template("signup.html",data=data)
            elif not len(password) > 6 :
                data["message"] = "password length should greater than 6"
                return render_template("signup.html",data=data)
    return render_template('signup.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password") 
    if request.method == "POST":
        cursor = con.cursor()
        cursor.execute("SELECT id FROM user_info WHERE username = %s AND password = %s", (username, password))
        user_id = cursor.fetchone()
        data = {
        "message": "Successfully logged in"  
                }
        if user_id:
            return render_template('home.html',data=data)
        else:
            data["message"] = "Invalid username or password"
            return render_template('home.html',data=data)
    return render_template('home.html')



if __name__ == "__main__":
    con = get_sql_conn()
    app.run(debug=True)