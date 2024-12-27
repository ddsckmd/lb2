from flask import Flask, request

app = Flask(__name__)

@app.route("/currency", methods=["GET"])
def get_currency():

    # Перевірка передачі параметра today
    if "today" in request.args:
        return "USD - 41.5 грн!"
    else:
        return "Параметр не передано >:("

if __name__ == '__main__':
    app.run(port=8000)
