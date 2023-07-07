from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Ciao sono stato deployato!"

    if __name__ == '__main__':
        app.run(debug= true,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))