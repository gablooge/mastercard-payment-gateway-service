from urllib.parse import urlencode
import requests
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def send_checkout_request():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'apiPasswor':''
    }
    api_password="ac35b2803b5ddb1b71442d0b3835e4fd"
    api_username="merchant.950028381"
    merchant="TEST950028381"
    operation="INITIATE_CHECKOUT"
    order_id='123'
    amount="100.00"
    currency="USD"
    data = {
        "apiOperation": operation,
        "apiPassword": api_password,
        "apiUsername": api_username,
        "merchant":merchant,
        "interaction.operation":"AUTHORIZE",
        "interaction.returnUrl":'http://localhost/checkout',
        "order.id":order_id,
        "order.amount":amount,
        "order.currency":currency
    }
    try:
        response = requests.post('https://ap-gateway.mastercard.com/api/nvp/version/63',headers=headers,data=urlencode(data))
       #get session id
        session_id =str(response.content).split('&')[2].split('=')[1]
        #todo validate session_id
        return render_template("template.html",session_id=session_id)
    except Exception as e:
        print(e)
        return "failed"

if __name__ == '__main__':
    app.run(debug=True)