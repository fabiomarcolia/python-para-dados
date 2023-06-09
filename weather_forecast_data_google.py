import requests
from bs4 import BeautifulSoup

city = "Jaipur" # enter city name

# creating url and requests instance
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs=f'class': 'BNeawe iBp4i AP7Wnd')).text
str = soup.find('div', attrs=f'class': 'BNeawe tAd8D AP7Wnd']).text

data = str.split('In')
time= data[0]
sky = data[1]

listdiv = soup.findAll('div', attrs=f'class': 'BNeawe s3v9rd AP7Wnd']
strd = listdiv[5].text
pos = strd.find( 'Wind')

other_data = strd[pos:]
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)

