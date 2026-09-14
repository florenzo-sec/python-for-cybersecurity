"""
Site Checker
Verify if a website is reacheable.
Asks for an URL and gives back status code, response time and the first 200 characters of the body.
Handles HTTPError(status code), ConnectionTimeout and ConnectionError(the server is unreacheable.)
"""


import requests

url = input("URL: ")
try:
    r = requests.get(url, timeout=5)
    r.raise_for_status()    
    
    print("Status code: " + str(r.status_code))
    print("Response time: " + str(r.elapsed))
    print("200 characters of the body: " + str(r.text[:200]))
    
except requests.exceptions.HTTPError as e:
    print("An HTTP error occured: " + str(e))
except requests.exceptions.ConnectTimeout:
    print("The connection timed out.")
except requests.exceptions.ConnectionError:
    print("The server isn't reacheable.")


