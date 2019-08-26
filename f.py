from flask import Flask
from flask import request
from flask import make_response
import json
import requests

#flask set up
app = Flask(__name__)
@app.route('/fare', methods=["GET","POST"])
def fare():
    re = request.get_json(silent=True, force=True)
    intentname = re["queryResult"]["intent"]["displayName"]
    if intentname == "number":
        return trainfare(intentname,re)
def trainfare(intentname,re):
    nunmber = re["queryResult"]["parameters"]["number"]
    #source=re["queryResult"]["parameters"]["source"]
    #dest=re["queryResult"]["parameters"]["destination"]
    q=re["queryResult"]["parameters"]["quota"]
    action=re["queryResult"]["action"]
    if q=="AC First Class":
        response=requests.get("http://indianrailapi.com/api/v2/TrainFare/apikey/63605ca44f54256173c0d3bf1d9101bc/TrainNumber/12565/From/SEE/To/NDLS/Quota/AC First Class").json()
        fare = response["Fares"][0]["Fare"]
    elif q == "AC 2-Tier":
        response = requests.get("http://indianrailapi.com/api/v2/TrainFare/apikey/63605ca44f54256173c0d3bf1d9101bc/TrainNumber/12565/From/SEE/To/NDLS/Quota/AC 2-Tier").json()
        fare = response["Fares"][1]["Fare"]
    elif q == "AC 3-Tier":
        response = requests.get("http://indianrailapi.com/api/v2/TrainFare/apikey/63605ca44f54256173c0d3bf1d9101bc/TrainNumber/12565/From/SEE/To/NDLS/Quota/AC 3-Tier").json()
        fare = response["Fares"][2]["Fare"]
    elif q == "Sleeper":
        response = requests.get("http://indianrailapi.com/api/v2/TrainFare/apikey/63605ca44f54256173c0d3bf1d9101bc/TrainNumber/12565/From/SEE/To/NDLS/Quota/Sleeper").json()
        fare = response["Fares"][3]["Fare"]
    elif q == "General":
        response = requests.get("http://indianrailapi.com/api/v2/TrainFare/apikey/63605ca44f54256173c0d3bf1d9101bc/TrainNumber/12565/From/SEE/To/NDLS/Quota/General").json()
        fare = response["Fares"][4]["Fare"]
    #c=len(response["Fares"]

    return train(fare, action)

def train(fare,action):
    if action=="TextResponse":
        return {
            "fulfillment": "The fare is "+str(fare)
        }


if __name__ == '__main__':
    app.run(port=3000,debug=True)