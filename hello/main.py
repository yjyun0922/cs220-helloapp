import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        try:
            return render_template('index.html', name=request.form["name"])
        except KeyError:
            return render_template('index.html', name="HTTP 400 Bad Request")
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
