from fastapi import FastAPI,UploadFile,File
import sqlite3
from pydantic import BaseModel
from classifier import predict_sentiment
import pandas as pd

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

@app.post("/predict/{text}")
def delete_record(text:str):
    sentiment = predict_sentiment(text)
    return{'message':sentiment}

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

@app.post("/bulk_insert")
def insert_csv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    connection = sqlite3.connect("../Comments.db")
    cursor = connection.cursor()
    df['sentiment']=df['comment_description'].apply(predict_sentiment)
    for i in range(0,len(df)):
        cursor.execute("INSERT into  Comments (comment_id,campaign_id,description,sentiment) values(?,?,?,?)",(int(df.iloc[i,1]),int(df.iloc[i,0]),df.iloc[i,2],df.iloc[i,3]))
        connection.commit()
    file.file.close()
    return {"filename": file.filename}