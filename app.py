from flask import Flask, request, jsonify
import openai
import italian_dictionary
from PyMultiDictionary import MultiDictionary
dictionary = MultiDictionary()

app = Flask(__name__)

openai.api_key = "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"
model = "text-davinci-003"
 
@app.route("/openAi/textSimilarity", methods=['GET'])
def textSimilarityCheck():
    category = request.args.get('category', type = str)
    text = request.args.get('text', type = str)
    result = calculate_cosine_similarity(category, text)
    return jsonify(result)
 
def calculate_cosine_similarity(category,text):
    response = openai.Completion.create(
        model=model,
        #prompt=f"semantic similarity cosin coefficient between: \n{category},\n{text}",
        prompt=f"Coefficiente similarita' semantica del coseno tra: \n{category},\n{text}. Rispondi solo con il valore float",
         temperature=0,
         max_tokens=34,
         top_p=1.0,
         frequency_penalty=0.0,
         presence_penalty=0.0
         )
    
    return response

@app.route("/openAi/wordExists", methods=['GET'])
def wordExistsCheck():
    text = request.args.get('text', type = str)
    result = check_if_word_in_dictionary(text)
    return {"Result" : f"{result}"}

def check_if_word_in_dictionary(word):
    result = dictionary.meaning('it', word)[1]
    if(result != ''):
        return True
    return False

# def check_if_word_in_dictionary(word):
#    try:
#        result = italian_dictionary.get_definition(word, limit=3, all_data=False) 
#        return True
#    except  Exception as e:
#        return False
    
#Api with path param (me is path param)
# class Echo(Resource):
#     def get(self, me):
#         return { "res": f"Text: {me}" }

#     def post(self, me):
#         return { "Answer": f"You said: {me}" }

# api.add_resource(Echo, '/echo')


#APi with json request
# @app.route("/openAi/wordExists", methods=['GET'])
# def wordExistsCheck(text:str):
#      input_json = request.get_json(force=True) 
#      text = input_json['text']
#      result = check_if_word_in_dictionary(text)
#      return jsonify(result)

#APi with json request
# @app.route("/openAi/textSimilarity", methods=['GET'])
# def textSimilarityCheck():
#      input_json = request.get_json(force=True) 
#      category = input_json['category']
#      text = input_json['text']
#      result = calculate_cosine_similarity(category, text)
#      return jsonify(result)

    