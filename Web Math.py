import requests
import bs4
import webbrowser
import hashlib as h

# Send a GET request using the session
session = requests.Session()
res = session.get("http://challenges.ringzer0team.com:10032/", cookies={'PHPSESSID':"3cv5giunpunbqutduf6icp4571"})

# Parse the HTML response using BeautifulSoup
soup = bs4.BeautifulSoup(res.text,"lxml")

# Extract the message from the HTML
message = soup.select_one(".message").getText()

# Remove unnecessary characters from the message
message = message.replace('----- BEGIN MESSAGE -----', '').replace('----- END MESSAGE -----', '')
message = message.replace('\n','').replace(' ','').replace('?','').replace('=','').replace('+',' ').replace('-',' ')

#Split 
liste=message.split(' ')

#Convert to decimal
num0=int(liste[0])
num1=int(liste[1],16)
num2=int(liste[2],2)

#Add all
Eq=num0+num1-num2

# Construct a new URL with the value
url = fr"http://challenges.ringzer0team.com:10032/?r={Eq}"

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
