import requests
from bs4 import BeautifulSoup as bs

gh_user = input('Enter Github username: ')

##SENDING REQUEST##
url = 'https://github.com/'+gh_user

##GETS REQUEST##
r = requests.get(url)

##GETS WHOLE HTML AND PARSED IT IN THE HTML PARSER##
soup = bs(r.content, 'html.parser')

##IN THE WHOLE HTML FIND THE PARTICULAR DATA USING .FIND AND TO GET THI IMAGE GOT THE SRC FILE##
profile_img = soup.find('img' , {'alt':'Avatar'})['src']

##PRINT THE IMAGE LINK##
print(profile_img)