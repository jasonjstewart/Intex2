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
def process_request(request, prescriberid):
    # Saves prescriber object
    prescriber = smod.Prescriber.objects.get(prescriberid=prescriberid)

    # Returns list of drugs prescribed by doctor
    drugs = {}
    drugs_id = {}
    drugs_is_opioid = {}
    for item in smod.Triple.objects.filter(prescriberid=prescriberid):
        drugs[item.drugname.drugname] = item.qty
        drugs_id[item.drugname.drugname] = item.drugname.drugid
        drugs_is_opioid[item.drugname.drugname] = item.drugname.isopioid

    # Grabs average drugs prescriptions
    average_prescription = {}
    for item in drugs:
        average_prescription[item] = int(smod.Triple.objects.filter(drugname=item).aggregate(Avg('qty'))['qty__avg'])

    # begin similar docs code block #

    url = "https://ussouthcentral.services.azureml.net/workspaces/382fad6769bc4a338bcdf681eec04cda/services/08c86c9c727e4b268c4293216230aa02/execute"

    querystring = {"api-version":"2.0","details":"true"}

    payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"PrescriberID\",\r\n        \"DrugName\",\r\n        \"Qty\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + prescriberid + "\",\r\n          \"value\",\r\n          \"0\"\r\n        ]\r\n      ]\r\n    }\r\n  },\r\n  \"GlobalParameters\": {}\r\n}"
    headers = {
        'Authorization': "Bearer HtW5FREgQONeZ/MzE20JLq9pBebUv+psXeveBwLddyYa+mg5OMKeI6EpT+k26qhX1+Vd5Mz0/I6nppIly0zlxA==",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "f03f6615-d4ae-4f09-ac98-066729d912df"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    jresponse = json.loads(response.text)

    docids = jresponse["Results"]["output1"]["value"]["Values"][0]

    docs = []

    for docid in docids:
        docs.append(smod.Prescriber.objects.get(prescriberid=docid))

    # end similar drugs code block #
    
    
    context = {
        'docs': docs,
        'prescriber': prescriber,
        'drugs': drugs,
        'drugs_id': drugs_id,
        'drugs_is_opioid': drugs_is_opioid,
        'average_prescription': average_prescription,
    }

    return request.dmp.render('prescriberProfile.html', context)        