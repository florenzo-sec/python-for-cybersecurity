import requests

url = input("URL: ")
try:
    r = requests.get(url,timeout=5)
    r.raise_for_status()

    security_headers = ['Content-Security-Policy','X-Frame-Options','Strict-Transport-Security','X-Content-Type-Options']

    for h in security_headers:
        if h in r.headers:
            print(h + " = " + r.headers[h])
        else:
            print(h + " MANCANTE")
            
except requests.exceptions.HTTPError as e:
    print("An HTTP error occured: " + str(e))
except requests.exceptions.ConnectTimeout:
    print("The connection timed out.")
except requests.exceptions.ConnectionError:
    print("The server isn't reacheable.")      
