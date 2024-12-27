import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/currency", methods=["GET"])
def get_currency():
    # Параметр param з URL
    param = request.args.get("param")

    # URL для запиту до API НБУ
    nbu_api_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

    # Визначаємо дату для today/yesterday
    if param == "today":
        date = ""  # Значення на today
    elif param == "yesterday":
        from datetime import datetime, timedelta
        date = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d") # Значення на yesterday: функція на зараз - один день від сьогодні і в формат рік-місяць-день
    else:
        return "Invalid parameter. Use 'param=today' or 'param=yesterday'"

    # Запит до API НБУ
    params = {"valcode": "USD", "date": date, "json": ""}
    response = requests.get(nbu_api_url, params=params)

    # Перевірка роботи
    if response.status_code == 200:
        data = response.json()
        if data:
            usd_rate = data[0]["rate"]
            return f"Курс USD - {usd_rate} грн."
        else:
            return "Нічого не знайдено."
    else:
        return "Помилка запиту до API НБУ."

if __name__ == '__main__':
    app.run(port=8000)
