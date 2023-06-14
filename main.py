import requests
from send_email import send_email

topic = "tesla"

api_key = "api_key for newsapi"
url = "https://newsapi.org/v2/" \
      "everything?" \
      f"q={topic}" \
      "&sortBy=publishedAt" \
      "&apiKey=api_key for newsapi" \
      "&language=en"

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"][:20]:
    # message+= article["title"]+"\n"+article["description"]
    # message= u'\n'.join((article["title"],article["description"])).encode('utf-8')

    body = "Subject: Today's news" + "\n"
    body + article["title"] + "\n" \
    + article["description"] + "\n" \
    + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
