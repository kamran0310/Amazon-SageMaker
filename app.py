#flask app for hellow world

from flask import Flask
import os

app=Flask(__name__)
@app.route('/', methods=['GET'])

def home():
    return "Hellow world"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)