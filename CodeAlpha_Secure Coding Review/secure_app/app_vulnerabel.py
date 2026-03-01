from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # ❌ VULNERABLE TO SQL INJECTION
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        return "Login Successful"
    else:
        return "Invalid Credentials"

if __name__ == "__main__":
    app.run(debug=True)
