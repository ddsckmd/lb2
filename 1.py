from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Khalina!"

if __name__ == '__main__':
    app.run(port=8000)