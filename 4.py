from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/content", methods=["GET"])
def handle_headers():
    # Отримати тип контенту через URL-параметр
    content_type = request.args.get("type", "text")

    if content_type == "json":
        # Відповідь у вигляді JSON-документу
        return jsonify(message="Формат JSON")
    elif content_type == "xml":
        # Відповідь у вигляді XML-документу
        return "<message>Формат XML</message>", {"Content-Type": "application/xml"}
    else:
        # Якщо параметр не вказано або інший
        return "Текстовий формат"

if __name__ == '__main__':
    app.run(port=8000)
