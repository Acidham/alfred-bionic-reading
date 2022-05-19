#!/usr/bin/python

import os
import sys
import urllib.parse

import requests

url = "https://bionic-reading1.p.rapidapi.com/convert"
html_path = "/tmp/bionic.html"

api_key = os.getenv('api_key') if os.getenv('api_key') is not None else ""
content = sys.argv[1]
content_enc = urllib.parse.quote(content)

if api_key != str():
    payload = f"content={content_enc}&response_type=html&request_type=html&fixation=1&saccade=10"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Host": "bionic-reading1.p.rapidapi.com",
        "X-RapidAPI-Key": f"{api_key}"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    output_content = ('<html>'
                      '<body style="'
                      'font-family: Arial;'
                      'font-size: 16pt; '
                      'color: black; '
                      'background-color: #F2F2F7; '
                      'width: 95%; '
                      'line-height: 1.5;">'
                      f'{response.text}'
                      '</body></html>')
else:
    output_content = 'API Key not set: https://rapidapi.com/bionic-reading-bionic-reading-default/api/bionic-reading1/'

with open(html_path, "w") as f:
    f.write(output_content)

sys.stdout.write(html_path)
