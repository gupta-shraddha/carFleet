import requests
import urllib
import sys
from requests.auth import HTTPDigestAuth
import json
import socket


def getDetailData(id):
    #personal api key must be used to access this information
    api_key = input("Enter you API Key")
    base_url = "http://creativecommons.tankerkoenig.de/json/detail.php?"
    url = base_url+'id='+id+'&apikey='+api_key
    print(url)
    try:
        response = requests.get(url, timeout=None).json()
    except:
        print('Exception occur: ', sys.exc_info()[0])

    data = response.json()
    print(data)
    if (response.ok):

        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(response.content)

        print("The response contains {0} properties".format(len(jData)))
        print("\n")
        for key in jData:
            print(key + " : " + jData[key])
    else:
        # If response code is not ok (200), print the resulting http error code with description
        response.raise_for_status()

def main():
    id = '8e04a261-815f-43f8-a5ba-20d12c5b3273'
    getDetailData(id)

if __name__ == '__main__':
    main()