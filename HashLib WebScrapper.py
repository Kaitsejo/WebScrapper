import requests
import bs4
import webbrowser
import hashlib as h

# Create a new session
session = requests.Session()

# Send a GET request using the session
res = session.get("http://challenges.ringzer0team.com:10013/")

# Parse the HTML response using BeautifulSoup
soup = bs4.BeautifulSoup(res.text,"lxml")

# Extract the message from the HTML
message = soup.select_one(".message").getText()

# Remove unnecessary characters from the message
message = message.replace('----- BEGIN MESSAGE -----', '').replace('----- END MESSAGE -----', '')
message = message.replace('\n','').replace(' ','')

# Print the message
print(message)

# Hash the message with SHA-512
hash_object = h.sha512(message.encode())
hex_dig = hash_object.hexdigest()

# Print the hash value
print(hex_dig)

# Construct a new URL with the hash value
url = fr"http://challenges.ringzer0team.com:10013/?r={hex_dig}"

# Send a GET request to the new URL using the session
res = session.get(url)

# Open the new URL in a web browser
webbrowser.open(url)

