import openai
from flask import Flask, render
_
template, jsonify, request
from flask
_
cors import CORS
import requests
app = Flask(__
name
__)
CORS(app)
# Configuración de la API de OpenAI
openai.api
_
key = "TU
_
API
_
KEY
_
OPENAI"
# Configuración de las APIs externas
API
_
KEYS = {
"thesportsdb": "YOUR
_
THE
_
SPORTS
_
DB
_
KEY"
,
"ufc
_
stats": "API
_
ENDPOINT"
,
"tapology": "API
_
ENDPOINT"
}
@app.route('/')
def home():
return render
_
template('index.html')
@app.route('/ai-chat'
, methods=['POST'])
def ai
_
chat():
user
_
input = request.json.get("message")
response = openai.ChatCompletion.create(
model="gpt-3.5-turbo"
,
messages=[{"role": "user"
,
"content": user
_
input}]
)
return jsonify(response["choices"][0]["message"]["content"])
@app.route('/events')
def get
_
events():
ufc
_
url = "https://ufc-data-api.ufc.com/api/v3/events"
response = requests.get(ufc
_
url)
events = response.json()
return jsonify(events)
if
__
name
__
== '
__
main
__
':
app.run(debug=True)
