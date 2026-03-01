from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = "SELECT password FROM users WHERE username=?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result:
        stored_password = result[0]

        if password == stored_password:
            return "Login Successful"

    return "Invalid Credentials"

if __name__ == "__main__":
    app.run(debug=True)
