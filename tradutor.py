import requests
from api_key import api_key
url = "https://text-translator2.p.rapidapi.com/translate"
text = input('Insira texto para ser traduzido:

)
payload =
"source_language": "pt"
"target_language": "en"
"text": text
  
headers =
"content-type": "application/x-www-form-urlencoded",
"X-RapidAPI-Key": api_key,
"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
response = requests.post(url, data=payload, headers=headers)
print(response. json( )['data']['translatedText'])
