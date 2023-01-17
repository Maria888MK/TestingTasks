# import required libraries
from urllib.request import urlopen
import time
import json
import requests

while(True):
    
    # source URL to retrieve the data
    url = "https://www.reddit.com/r/subreddit.json"
    # put your webhook url here
    webhook_url = "https://webhook.site/d04790e1-e1c6-49d6-b072-d3fbdcff4162"

    # store the response of URL
    response = urlopen(url)

    # storing the JSON response from url in data
    data_json = json.loads(response.read())

    # for reading nested data finding the total number of elements in dictionary
    elements = data_json['data']['dist']

    # create an empty dictionary to store data
    extracted_data = dict()

    # populate the dictionary with the extracted data (title, url) from json
    for i in range(elements):
        title = data_json['data']['children'][i]['data']['title']
        url_from_json = data_json['data']['children'][i]['data']['url']
        extracted_data[title] = url_from_json

    # push the data to webhook.site
    r = requests.post(webhook_url, data=json.dumps(extracted_data, indent=2),headers={'title':'url'})

    # repeat the entire skript each minute
    time.sleep(60)
