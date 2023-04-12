from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)
 

@app.route('/',methods=['GET','POST'])

def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        phone= request.form['num']
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (Name, Password,email,Phone) VALUES (?, ?, ?,?)", (name, password, email,phone))
        connection.commit()
        connection.close()
        
        
    return render_template('register.html')
   
 

if __name__ == '__main__':
 
    app.run()