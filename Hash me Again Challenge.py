import requests
import bs4
import webbrowser
import hashlib as h

# Send a GET request using the session
session = requests.Session()
res = session.get("http://challenges.ringzer0team.com:10014/", cookies={'PHPSESSID':"3cv5giunpunbqutduf6icp4571"})

# Parse the HTML response using BeautifulSoup
soup = bs4.BeautifulSoup(res.text,"lxml")

# Extract the message from the HTML
message = soup.select_one(".message").getText()

# Remove unnecessary characters from the message
message = message.replace('----- BEGIN MESSAGE -----', '').replace('----- END MESSAGE -----', '')
message = message.replace('\n','').replace(' ','')

#binary to bytes
message_bytes = int(message, 2).to_bytes((len(message) + 7) // 8, 'big')

# Hash the message with SHA-512
hash_object = h.sha512(message_bytes)
hex_dig = hash_object.hexdigest()

# Construct a new URL with the hash value
url = fr"http://challenges.ringzer0team.com:10014/?r={hex_dig}"

# Send a GET request to the new URL using the session
res = session.get(url, cookies={'PHPSESSID':"3cv5giunpunbqutduf6icp4571"})

# Get the html content
soup = bs4.BeautifulSoup(res.text,"lxml")

#Get the Flag
flag = soup.select('.alert')
if flag:
    print(flag[0].getText())
else:
    print("Flag not found")
