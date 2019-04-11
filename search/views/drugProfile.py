from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from search import models as smod
from django import forms
from django.http import HttpResponseRedirect
from django.db import connection
from django.utils.html import escape
from django.db.models import Avg
import requests, json

@view_function
def process_request(request, drugid):
    # Saves prescriber object
    drug = smod.Drugs.objects.get(drugid=drugid)

    definition = "No definition available for this drug."
    # define = drug.drugname
    # define = define.replace(".", " ")
    # define = define.lower()
    # defines = define.split(" ")
    # defines.reverse()
    # defines.append(define)
    # defines.reverse()
    # done = False

    # for define in defines:
    #     if not done:
    #         url = "https://od-api.oxforddictionaries.com/api/v1/entries/en/" + define

    #         payload = ""
    #         headers = {
    #             'app_id': "edfc361b",
    #             'app_key': "77733d17a98f8f2928ee550aea04f4ca",
    #             'cache-control': "no-cache",
    #             'Postman-Token': "fa4cf12f-6c89-495a-b5bc-8efca550ea55"
    #         }

    #         response = requests.request("GET", url, data=payload, headers=headers)

    #         if response.status_code != 404:
    #             done = True
    #             jresponse = json.loads(response.text)
    #             if 'definitions' in jresponse['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]:
    #                 definition = jresponse['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]["definitions"][0]
    #             elif 'short_definitions' in jresponse['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]:
    #                 definition = jresponse['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]["short_definitions"][0]
    #             elif 'crossReferenceMarkers' in jresponse['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]:
    #                 definition = jresponse['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]["crossReferenceMarkers"][0]
    #             else:
    #                 done = False


    # Returns list of drugs prescribed by doctor
    prescribers = {}
    for item in smod.Triple.objects.filter(drugname=drug.drugname).order_by('-qty')[:10]:
        prescribers[item.prescriberid] = item.qty

    # Grabs average drugs prescriptions
    average_prescription = int(smod.Triple.objects.filter(drugname=drug.drugname).aggregate(Avg('qty'))['qty__avg'])

    url = "https://ussouthcentral.services.azureml.net/workspaces/382fad6769bc4a338bcdf681eec04cda/services/a7487579ef62453cb8f123d2d2b531ab/execute"

    querystring = {"api-version": "2.0", "details": "true"}

    payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"ID\",\r\n        \"PrescriberID\",\r\n        \"DrugName\",\r\n        \"Qty\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"0\",\r\n          \"0\",\r\n          \"ABILIFY\",\r\n          \"0\"\r\n        ]\r\n      ]\r\n    }\r\n  },\r\n  \"GlobalParameters\": {}\r\n}"
    headers = {
        'Authorization': "Bearer frYM5C+NQlZuc1aHZ0GUgj0y3zRY2vIPg7PjTXi+HXrNJGy47NHlAcfG15xnJriVmeMjew7M95pyfKFzaoQ5AA==",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "aece4052-6be6-4293-a6f4-8a70ee881a81"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    jresponse = json.loads(response.text)

    similar_drugs = jresponse["Results"]["output1"]["value"]["Values"][0]

    drugs = []
    for drug in similar_drugs:
        drugs.append(smod.Drugs.objects.get(drugname=drug))
    print("\n\n\n\n\n\n\n")
    print(type(drugs))
    print(type(definition))
    print(type(drug))
    print(type(prescribers))
    print(type(average_prescription))

    context = {
        'drugs': drugs,
        'definition': definition,
        'drug': drug,
        'prescribers': prescribers,
        'average_prescription': average_prescription,
    }

    return request.dmp.render('drugProfile.html', context)