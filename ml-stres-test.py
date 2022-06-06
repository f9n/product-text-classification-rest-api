import sys

import requests


data1 = ['Elma']
data3 = ['Elma', 'Telefon', 'Yumurta']
data5 = ['Elma', 'Telefon', 'Televizyon', 'Yumurta', 'Peynir']
data10 = ['Elma', 'Telefon', 'Televizyon', 'Yumurta', 'Peynir', 'Ekmek', 'Pizza', 'Laptop', 'Radyo', 'Tablet']


def ml_analysis(data):
    r = requests.post('https://product-text-clss-rest-api.herokuapp.com/classification', json=data)
    print(r.json())
    print(r.elapsed)


if sys.argv[1] == '1':
    ml_analysis(data1)
elif sys.argv[1] == '3':
    ml_analysis(data3)
elif sys.argv[1] == '5':
    ml_analysis(data5)
elif sys.argv[1] == '10':
    ml_analysis(data10)
else:
    ml_analysis(data1)
