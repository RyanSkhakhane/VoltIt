import hashlib
import stdiomask
import sqlite3


#set up connection to the DB
conn = sqlite3.connect('creds.db')



def createTable():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            service TEXT NOT NULL,
            email TEXT ,
            password TEXT NOT NULL
        )
    ''')
    cursor.close()
    conn.close()


def add_pwd_to_db():
    cursor = conn.cursor()
    Name ,password ,Email = pwdInput()
    Email = hashlib.sha256.
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (Name, Email, password))
    print('success')
    conn.commit()
    cursor.close()
    conn.close()


def hash_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def pwdInput():
    serviceName = input("Enter Service name: ")
    email = input('Enter associated email: ')
    password = stdiomask.getpass("Enter your password: ", mask='.')
    return serviceName,email,password


def fetchFromDb(ServiceName):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (ServiceName,))
    rows = cursor.fetchall()
    print(rows[0][3])
    cursor.close()
    conn.close()    
    return rows

def updatePwd():
    serviceName, Email ,pwd = pwdInput()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password =? Where username = ?",(pwd, serviceName))


