from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from query import query_model

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.post("/")
@cross_origin()
def get_prediction():
  if request.is_json:
    req = request.get_json()
    result = query_model(req["age"], req["education"], req["percent"])
    return jsonify({ "proficiency": result }), 200
  return {"error": "Invalid request"}, 415