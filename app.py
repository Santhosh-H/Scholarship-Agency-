from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)
 

@app.route('/',methods=['GET','POST'])

def register():
    print("1")
    if request.method == 'POST':
        print("2")
        name = request.form['name']
        print("3")
        password = request.form['password']
        email = request.form['email']
        phone= request.form['num']
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (Name, Password,email,Phone) VALUES (?, ?, ?,?)", (name, password, email,phone))
        connection.commit()
        connection.close()
        print("Data Added successfully")
        #return redirect('/index1')
        return render_template('index1.html')
    return render_template('register.html')
    
   


if __name__ == '__main__':
 
    app.run()