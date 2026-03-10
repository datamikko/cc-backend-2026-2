from flask import Flask, request
import pickle

app = Flask(__name__)

with open("sentiment_model_v1.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def health():
    return {"message": "alive again even more"}

@app.route("/api", methods=["POST"])
def sentiment_api():
    data = request.get_json()
    print(data)
    print(model.predict([data["sentiment"]]))
    return {"sentence": data["sentiment"], "sentiment": "positive"}
