import requests
import os
from decouple import config

# Set your Unsplash access key here


# Set the API endpoint URL and parameters
def fetchImage(query):
    access_key = config("UNSPLASH_API_KEY")
    url = "https://api.unsplash.com/photos/random/"
    params = {
        "query": query,
        "orientation": "landscape",
        "client_id": access_key,
        "count": 1,
    }

    # Send the request and get the response
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and extract the photo URL
        photo_data = response.json()
        photo_urls = photo_data
        
        # Do something with the photo URL, like display it on your website or in your application
        for url in photo_urls:
            return url['urls']['regular']
    else:
        # Handle the case where the request failed
        print("Error: request failed with status code", response.status_code)