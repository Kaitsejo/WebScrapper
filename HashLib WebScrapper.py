import requests
import bs4
import webbrowser
import hashlib as h

# Send a GET request using the session
res = requests.get("http://challenges.ringzer0team.com:10013/", cookies={'PHPSESSID':"2jb43e3m489n7hpih5vfjgeotg"})

# Parse the HTML response using BeautifulSoup
soup = bs4.BeautifulSoup(res.text,"lxml")

# Extract the message from the HTML
message = soup.select_one(".message").getText()

# Remove unnecessary characters from the message
message = message.replace('----- BEGIN MESSAGE -----', '').replace('----- END MESSAGE -----', '')
message = message.replace('\n','').replace(' ','')

# Hash the message with SHA-512
hash_object = h.sha512(message.encode())
hex_dig = hash_object.hexdigest()

# Construct a new URL with the hash value
url = fr"http://challenges.ringzer0team.com:10013/?r={hex_dig}"

# Send a GET request to the new URL using the session
res = requests.get(url)

# Get the html content
soupe = bs4.BeautifulSoup(res.text,"lxml")
                          
#Get the Flag                                       
Flag=soupe.select('.alert')
print(Flag[0].getText())
