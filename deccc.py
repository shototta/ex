import requests

url = 'https://api.thecatapi.com/v1/images/search?limit=10'

url_cats = []
response = requests.get(url).json()
for line in response:
    url_cats.append(line['url'])

for i in range(10):
    file = open(f'cat{i}.jpg','wb')
    file.write(requests.get(url_cats[i]).content)
    file.close()

print(url_cats)