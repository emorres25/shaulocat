from django.shortcuts import render
import requests
import sys

# Create your views here.
YO_API = "https://api.justyo.co/yo/"
api_key = '006c7d21-b262-40e9-b243-d4082436f646'

def send_yo(username, link):
    """Yo a username"""
    requests.post(YO_API, data={'api_token': api_key, 'username': username, 'link': link})

def yo():
    """Handle callback request"""

    username = request.args.get('username')
    location = request.args.get('location')
    splitted = location.split(';')
    # Parse latitude and longitude from request params
    latitude = splitted[0]
    longitude = splitted[1]
    
    requests.post(YO_API, data={'api_token': '3u3XKTW9CvPJxUj90w94ZbZ1QoE0LR', 'username': username, 'text' : 'ssup'})
    return 'OK'