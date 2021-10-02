from data import Data
from bottle import run, post, request
from django.http import HttpResponse
from django.conf import settings
import django
import json
import csv


@post("/server2/calculate")
def do():
    print(str(request))
    dataFromServer1 = json.load(request.body)
    print("############")
    print(request.body)

    responseNumber = dataFromServer1.get("Number") * 3

    print("#####################")
    print(responseNumber)

    responseString = "Number\n"

    responseString+= str(responseNumber)

    return responseString


#django test
@post("/server2/calculate/django/static")
def do():
    if not settings.configured:
        settings.configure(DEFAULT_CHARSET="utf-8")
    #django.setup()
    dataFromServer1 = json.load(request.body)
    responseNumber = dataFromServer1.get("Number") * 3

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="response.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Number', f'{responseNumber}'])
    #writer.writerow([])

    return response

@post("/server2/calculate/django/dynamic")
def do():
    if not settings.configured:
        settings.configure(DEFAULT_CHARSET="utf-8")
    #django.setup()
    dataFromServer1 = json.load(request.body)

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="response.csv"'},
    )

    writer = csv.writer(response)
    for attr, value in dataFromServer1.items():
        if (type(value) == int):
            value = value * 3
        writer.writerow([str(attr), value])
    #responseNumber = dataFromServer1.get("Number") * 3

    

    
    #writer.writerow(['Number', f'{responseNumber}'])
    #writer.writerow([])

    return response
    
    


run(host="127.0.0.1", port="4444", debug=True, reloader=True)

#run(host="127.0.0.1", port=4444, debug=True, reloader=True, server="paste")