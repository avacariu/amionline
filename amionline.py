from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return send_file('index.html')

@app.route('/<uuid>')
def get(uuid):
    return uuid

if __name__ == "__main__":
    app.run(debug=True)
