===============================
SECURE CODING REVIEW PROJECT
===============================

Project Title:
Secure Coding Review of a Simple Flask Login Application

--------------------------------
1. Project Description
--------------------------------
This project demonstrates a secure coding review of a basic web login application written in Python using the Flask framework. 

The initial version of the application contains serious security vulnerabilities, primarily SQL Injection, due to unsafe concatenation of user inputs in SQL queries and storing passwords in plaintext.

The secure version applies parameterized queries to prevent SQL injection attacks and implements proper login validation.

This review highlights common security flaws, how they can be exploited, and how to fix them to build safer applications.

--------------------------------
2. Environment Setup
--------------------------------
Operating System:
- Kali Linux (preferred for testing and development)

Software and Libraries:
- Python 3
- Flask
- SQLite3
- bcrypt (optional for password hashing)

Installation commands:

sudo apt update
sudo apt install python3-pip
pip3 install flask bcrypt

--------------------------------
3. Application Files
--------------------------------
- app_vulnerable.py : Insecure login application vulnerable to SQL Injection.
- app_secure.py     : Secure login application using parameterized queries.
- users.db          : SQLite database with user credentials.

--------------------------------
4. How to Run
--------------------------------
Step 1: Create and populate the SQLite database (run Python shell):

    python3
    >>> import sqlite3
    >>> conn = sqlite3.connect('users.db')
    >>> cursor = conn.cursor()
    >>> cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    >>> cursor.execute("INSERT INTO users VALUES ('admin', 'admin123')")
    >>> conn.commit()
    >>> conn.close()
    >>> exit()

Step 2: Run the vulnerable app:

    python3 app_vulnerable.py

Step 3: Test login at:

    http://127.0.0.1:5000/login?username=admin&password=admin123

Try SQL injection:

    http://127.0.0.1:5000/login?username=admin' --&password=anything

Step 4: Stop the vulnerable app (Ctrl+C) and run the secure app:

    python3 app_secure.py

Step 5: Test the same URLs again. SQL injection should fail in the secure app.

--------------------------------
5. Security Vulnerabilities Found
--------------------------------
- SQL Injection due to unsafe string formatting in SQL query.
- Plaintext storage of passwords.
- No input validation or sanitization.
- Lack of error handling.

--------------------------------
6. Fixes Implemented
--------------------------------
- Parameterized SQL queries to prevent injection.
- Proper login validation.
- (Optional) Password hashing recommended for real apps.
- Code structured for clarity and security.

--------------------------------
7. Recommendations
--------------------------------
- Always use parameterized queries or ORM tools.
- Hash passwords with secure algorithms like bcrypt.
- Validate and sanitize user inputs.
- Implement comprehensive error handling.
- Use HTTPS for secure communication.

--------------------------------
8. Learning Outcomes
--------------------------------
- Understanding of SQL Injection attack and mitigation.
- Practical experience securing web applications.
- Awareness of secure coding best practices.
- Hands-on usage of Flask and SQLite on Kali Linux.

--------------------------------
9. Author and Date
--------------------------------
Author: [Ezaz Ahmed]
Date: [01 March,2026]

--------------------------------
Important Note:
--------------------------------
This project is for educational purposes only. Do not deploy insecure applications in production environments. Always follow ethical guidelines and obtain permission before testing real systems.
