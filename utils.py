from flask import Response
import requests


def currency_calc(cur):
    response = requests.get('https://bitpay.com/api/rates')
    data = response.json()

    for values in data:
        if values.get('code') == cur.upper():
            return values.get('name') + ' - ' + str(values.get('rate'))

    return Response('Error: incorrect parameter.', status=400)
