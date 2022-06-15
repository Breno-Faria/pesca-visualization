from flask import Flask, render_template, url_for, redirect, request
import psycopg2
import os

app = Flask(__name__)

def connect_to_db():
    connection = psycopg2.connect(
        host=os.environ['host'],
        database=os.environ['database'],
        port=os.environ['port'],
        user=os.environ['user'],
        password=os.environ['password'],
    )
    return connection

@app.route("/")
def home():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM contas ORDER BY id DESC'
    )
    accounts = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("index.html", accounts=accounts)