from locale import currency

from flask import Flask,request

app = Flask (__name__)

@app.route("/")
def handle_get ():
    #логіку якусб
    return "Hello World!"

@app.route("/path")
def handle_post ():
    return "another path"

@app.route("/currency")
def handle_currency_req ():
    print(request.args)
    print(request.args.getlist("currency"))
    if request.args.getlist("currency") == "usd":
        #посилання на нбу; конвертуємо (NBU^ get response with cuurencies)
        #create local response
        return "41.5"

    print(type(request.headers))
    print(request.headers.get("Content-Type"))
    if request.headers.get("Content-Type") == "application/json":
        return "json"
    elif request.headers.get("Content-Type") == "application/xml":
        return "xml"
    else:
        return "text"


    return "currency"

app.run()