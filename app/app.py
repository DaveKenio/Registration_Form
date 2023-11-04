from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, "/static")
##app.__static_folder__ = 
# MySQL configurations
mydb = mysql.connector.connect(
  host="127.0.0.1",  # Change this to your MySQL server name if different
  user="root",   # Change this to your MySQL username
  password="dave2001",  # Change this to your MySQL password
  database="registration",  # Change this to your MySQL database name
  auth_plugin='mysql_native_password'
)

@app.route('/')
def registration_form():
    return render_template('main.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']
    gender = request.form['gender']
    dob = request.form['dob']
    marital_status = request.form['marital_status']
    password = request.form['password']

    cursor = mydb.cursor()
    sql = "INSERT INTO users (first_name, last_name, email, phone, address, gender, dob, marital_status, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (first_name, last_name, email, phone, address, gender, dob, marital_status, password)
    cursor.execute(sql, val)

    mydb.commit()
    cursor.close()

    return 'Form submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)