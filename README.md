### Bert Fine tuning for sentiment classification

## Install dependencies
all dependencies are in the requirement file, install by runing this on terminal

pip install -r requirements.txt

## Runing backend 

- to run backend, first make sure you are in the backend directory
- run the command

uvicorn app:app --reload

## Test the endpoints
to test the end points I used postman, I uploaded the collection file of the queries

## Necessary changes to run the project
You can find the multilingual bert model and preprocessor model to use in these links :
- link for the bert model "multi-cased-l-12-h-768-a-12" :
https://www.kaggle.com/models/tensorflow/bert/frameworks/TensorFlow2/variations/multi-cased-l-12-h-768-a-12/versions/4
- link for the bert multi-cased-preprocessor :
https://kaggle.com/models/tensorflow/bert/frameworks/TensorFlow2/variations/multi-cased-preprocess/versions/3
- Add bert model the this path "./model/Bert_model/bert_cased"
- Add bert preprocessor to this this path "./model/Bert_model/bert_multi_cased_preprocessor"
- Or you can add the links directly to the "./model/finetuning.ipynb" instead of model and preprocessor paths.

## Data issue
Due to some privacy issues of the data. I was not able to push the data to the repository(I wanted to make the project public)








