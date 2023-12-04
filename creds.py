from cryptography.fernet import Fernet
import stdiomask
import sqlite3
import json
import os


#set up connection to the DB
conn = sqlite3.connect('creds.sqlite')

with open('settings.json', 'r') as file:
    data = json.load(file)

key = data["key"]

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




def encrypt(value, key):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(value.encode())
    return cipher_text

def decrypt(value,key):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.decrypt(value.decode())
    return cipher_text


# UI/UX
def pwdInput():
    serviceName = input("Enter Service name: ")
    email = input('Enter associated email: ')
    password = stdiomask.getpass("Enter your password: ", mask='.')
    Password = encrypt(password, key)

    return serviceName,email,Password



#CRUD
"""
THIS SECTION IS DATABASE RELATED, SPECIFICALLY FOR "CRUD" OPERTIONS
"""
def CreatePwd():
    cursor = conn.cursor()
    Name ,email, password = pwdInput()
    cursor.execute("INSERT INTO users (service, email, password) VALUES (?, ?, ?)", (Name, email, password))
    print('success')
    conn.commit()
    cursor.close()
    conn.close()


def ReadPwd(ServiceName):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE service = ?", (ServiceName,))
    rows = cursor.fetchall()
    pwd = rows[0][3]
    Pwd = decrypt(pwd,key)
    print(Pwd)
    cursor.close()
    conn.close()    
    return Pwd


def UpdatePwd():
    serviceName, Email ,pwd = pwdInput()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password =? Where service = ?",(pwd, serviceName))
    conn.commit()
    cursor.close()
    conn.close()


def DeletePwd(serviceName):
    cursor = conn.cursor()
    cursor.execute("DETELE FROM users where service = ?", (serviceName))
    conn.commit()
    cursor.close()
    conn.close()

