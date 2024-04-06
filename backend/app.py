from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def get_data():
    return{'message':"Welcome to Home page"}

@app.post("/insert")
def insert_record():
    #insert a record into sqlite db with provided comment_id,campaign_id, description, sentiment
    return{'message':"new record inserted to database"}

@app.delete("/delete")
def delete_record():
    # delete comment from db based on comment_id
    return{'message':"record deleted"}

@app.patch("/update")
def update_record():
    # update a record based on provided comment_id,campaign_id, description, sentiment
    return{'message':"record updated successfuly"}

@app.post("bulk_insert")
def insert_csv():
    # uplaod a csv file containing comment_id,campaign_id and description, campute their sentiment and insert it to db
    return {'message':"csv file inserted succefully to the database"}