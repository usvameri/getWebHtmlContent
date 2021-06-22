from urllib import parse
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import random 

browser = webdriver.Chrome(r"C:\Users\usvameria\.wdm\drivers\chromedriver\win32\91.0.4472.19\chromedriver.exe")
urlFromUser = input("Enter a website url you want to get script: ")
websiteUrl ="https://www.sikayetvar.com/turk-telekom" 
if urlFromUser is not None:
    websiteUrl = urlFromUser
usernames = []
usernamee = set() #for adding value in other points 


def getHTML(url):
    # get html content of web page
    browser.get(websiteUrl)
    time.sleep(1) 
    browser.refresh
    page_source = browser.page_source
    browser.close()
    return page_source
def parseHTML(html_source):
    return BeautifulSoup(html_source,'html.parser')
def getArticles(soup):
    return  soup.find_all("article")
def getTitles(soup):
    return soup.find_all("complaint-title")
def getCounts(articles):
    print("Total Choisen Username Count:{totalChoisenUsername}".format(totalChoisenUsername = len(usernamee)))
    print("Total Content Count:{totalContentCount}".format(totalContentCount = len(articles)))
def startDrawing(articles):
    for article in articles:
        username = article.find("span",{"class":"username"})
        content = article.find("p")
        if username is not None and content is not None:
            if  "abone" in content.text.lower():
                usernames.append(username)
                usernamee.add(username.text)
                print(username.text + "; " + content.text)
                print("")



soup = parseHTML(getHTML(websiteUrl))
articles = getArticles(soup)
titles = getTitles(soup)
startDrawing(articles)
getCounts(articles)
print("Choisen :" + random.choice(list(usernamee)))


























"""
for comment in comments:
    print(len(comments))
    #author = comment.find("yt-formatted-string",{"id":"content-text"})
    author = comment.find("div",{"id":"content"})
    print(author)

for content in contents:
    print(content)
    x = content.find("yt-formatted-string",{"id":"content-text"}).text
    print(x)
    print("xaxaxa---------------")
"""

#usernames = soup.find_all("user-details")


#print(usernames)
