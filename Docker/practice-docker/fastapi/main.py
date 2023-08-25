import os
from decouple import config
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pymysql

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])

mysql_user = config("MYSQL_USER")
mysql_password = config("MYSQL_PASSWORD")
mysql_db = config("MYSQL_DB")
mysql_host = config("DBHOST", default="localhost")

def get_connection():
    return pymysql.connect(
        host=mysql_host,
        port=3306,
        user=mysql_user,
        password=mysql_password,
        db=mysql_db,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.get("/")
def index():
    return "Backend Server"

@app.get("/visits")
def read_visits():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM visits")
            results = cursor.fetchall()
            return {"visits": results}
    finally:
        connection.close()

class VisitInput(BaseModel):
    name: str

@app.post("/visits")
def write_visit(input_data: VisitInput):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO visits (visitor_name) VALUES (%s)", (input_data.name,))
            connection.commit()
        return "Visit added successfully!"
    finally:
        connection.close()

