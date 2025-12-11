# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("POSTGRES_DB", "mydb")
DB_USER = os.environ.get("POSTGRES_USER", "postgres")
DB_PASS = os.environ.get("POSTGRES_PASSWORD", "postgres")
DB_PORT = 5432

def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASS,
                port=DB_PORT
            )
            conn.close()
            print("Connected to DB")
            break
        except Exception:
            print("DB not ready, retrying in 2 seconds...")
            time.sleep(2)

wait_for_db()

@app.route("/info")
def info():
    return jsonify({"message": "Привіт з backend!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
