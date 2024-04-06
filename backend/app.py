from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel

class Comment(BaseModel):
    comment_id: int
    compaign_id : int
    comment_description: str
    sentiment : str
app=FastAPI()

@app.get("/")
def get_data():
    connection = sqlite3.connect("../Comments.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM Comments")
    record = cursor.fetchone()
    cursor.close()
    return{'message':record}

@app.post("/insert")
def insert_record(comment:Comment):
    connection = sqlite3.connect("../Comments.db")
    cursor = connection.cursor()
    cursor.execute("INSERT into  Comments (comment_id,campaign_id,description,sentiment) values(?,?,?,?)",( comment.comment_id,comment.compaign_id, comment.comment_description,comment.sentiment))
    connection.commit()
    return{'message':"Comment has been added to the database"}

@app.delete("/delete/{comment_id}")
def delete_record(comment_id:int):
    connection = sqlite3.connect("../Comments.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM  Comments WHERE comment_id= ?",(comment_id,))
    connection.commit()
    return{'message':"record deleted"}

@app.patch("/update")
def update_record(comment:Comment):
    connection = sqlite3.connect("../Comments.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Comments SET campaign_id=?, description=?,sentiment=? WHERE comment_id=?",(comment.compaign_id, comment.comment_description,comment.sentiment, comment.comment_id))
    connection.commit()
    # update a record based on provided comment_id,campaign_id, description, sentiment
    return{'message':"record updated successfuly"}

@app.post("bulk_insert")
def insert_csv():
    # uplaod a csv file containing comment_id,campaign_id and description, campute their sentiment and insert it to db
    return {'message':"csv file inserted succefully to the database"}