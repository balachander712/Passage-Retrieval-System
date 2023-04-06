from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import mysql.connector

app = FastAPI()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="test"
)

mycursor = mydb.cursor()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r") as file:
        return file.read()


@app.get("/data")
async def get_data(query: str):
    # execute the SQL query to fetch the data
    print(query)
    sql_query = "SELECT passage FROM passage_collection WHERE query = %s"
    mycursor.execute(sql_query, (query,))
    result = mycursor.fetchall()
    passage = result[0]
    print(passage)
    print(passage[0])


    # format the data as a list of dictionaries
    return passage[0]