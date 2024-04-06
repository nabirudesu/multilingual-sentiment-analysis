import tensorflow as tf
import tensorflow_hub as hub 
import tensorflow_text

classifier = tf.keras.models.load_model('classifier/')

def tokenize_data(text):
    tokenizer = hub.load('../model/bert_model/bert_multi_cased_preprocessor/')
    tokens= tokenizer.tokenize(tf.constant([text]))
    with tf.device('/CPU:0'):
        encoder_inputs = tokenizer.bert_pack_inputs(
            [tokens],
            seq_length=64)  # Optional argument.
    return [encoder_inputs['input_word_ids'],encoder_inputs['input_mask'],encoder_inputs['input_type_ids']]


def predict_sentiment(text):
    tokenizeed_comment= tokenize_data(text)
    classe_probability=classifier.predict({'input_word_ids':tokenizeed_comment[0],'input_mask':tokenizeed_comment[1],'input_type_ids':tokenizeed_comment[2]})
    if classe_probability<=0.5:
        sentiment='positive'
        return(sentiment)
    else:
        sentiment='negative'
        return(sentiment)