from flask import Flask, request, jsonify
import openai
from sklearn.metrics.pairwise import cosine_similarity
import italian_dictionary

app = Flask(__name__)

openai.api_key = "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"
model = "text-davinci-003"

@app.route("/openAi/textSimilarity", methods=['GET'])
def textSimilarityCheck():
     input_json = request.get_json(force=True) 
     category = input_json['category']
     text = input_json['text']
     result = calculate_cosine_similarity(category, text)
     return jsonify(result)
 
def calculate_cosine_similarity(category,text):
    response = openai.Completion.create(
        model=model,
        #prompt=f"semantic similarity cosin coefficient between: \n{category},\n{text}",
        prompt=f"Coefficiente similarita' semantica del coseno tra: \n{category},\n{text}. Rispondi solo con il valore float",
         temperature=0,
         max_tokens=64,
         top_p=1.0,
         frequency_penalty=0.0,
         presence_penalty=0.0
         )
    
    return response


@app.route("/openAi/wordExists", methods=['GET'])
def wordExistsCheck():
     input_json = request.get_json(force=True) 
     text = input_json['text']
     result = check_if_word_in_dictionary(text)
     return jsonify(result)

def check_if_word_in_dictionary(word):
    try:
        result = italian_dictionary.get_definition(word, limit=3, all_data=False) 
        return True
    except:
        return False

    