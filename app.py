from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
app = Flask(__name__)
 

@app.route('/register',methods=['GET','POST'])

def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        phone= request.form['num']
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (name))
        user = cursor.fetchone()
        print(user)
        try:
            # Hash the password
           
            cursor.execute("INSERT INTO users (Name, Password,email,Phone) VALUES (?, ?, ?,?)", (name, password, email,phone))
            connection.commit()
            connection.close()
        except:
            err_message="E-mail already registered!"
            return render_template('index.html')
        return redirect('/login')
    return render_template('index.html')
   
 

if __name__ == '__main__':
 
    app.run()