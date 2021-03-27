import requests
from bs4 import BeautifulSoup
import hashlib

url = 'http://178.62.54.33:31146/'

# send request to get the random string
s = requests.session()  # both GET & POST requests have to be in the same session

response = s.get(url)

html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

main_string = soup.find_all("h3")[0].text

# hash the random string
md5hash = hashlib.md5(main_string.encode()).hexdigest()

print(main_string)
print(md5hash)

# submit the hash
request_body = {'hash': md5hash}
print(request_body)

response = s.post(url, data=request_body)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
print(soup.prettify())
