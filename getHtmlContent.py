from urllib import parse
from selenium import webdriver
import keyboard
import time
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import random 

websiteUrl ="https://www.sikayetvar.com/turk-telekom" 


browser = webdriver.Chrome(r"C:\Users\usvameria\.wdm\drivers\chromedriver\win32\91.0.4472.19\chromedriver.exe")
urlFromUser = input("Enter a website url you want to get script: ")

if not urlFromUser:
      print("skipping.")
else:
    websiteUrl = urlFromUser

# if keyboard.is_pressed('enter'):
#     websiteUrl = urlFromUser


# if urlFromUser is not None and not "":
usernames = []
usernamee = set() #for adding value in other points 
isHtmlContentNeed = False
firstHtmlTag = "article"
secondHtmlTag = "complaint-title"


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
def getFirstTag(soup):
    try:
        return  soup.find_all(firstHtmlTag)
    except:
        print("Cant find any tag like you write")
def getTitles(soup):
        secondTags = soup.find_all(secondHtmlTag)
        print(len(secondTags))
        # try:
        for i in secondTags:
            targetTagInSecondTags = i.find("a",{"class":"complaint-layer"})
            print(targetTagInSecondTags.text)
         
        # except:
            # print("error************************************")
        return  targetTagInSecondTags
   
    # allt = soup.find_all(secondHtmlTag)
    # print(secondHtmlTag)
    # print("************** "+str(len(allt)))
    # return allt

def getCounts(firstTagResult):
    print("Total Choisen Username Count:{totalChoisenUsername}".format(totalChoisenUsername = len(usernamee)))
    print("Total Content Count:{totalContentCount}".format(totalContentCount = len(firstTagResult)))
def startDrawing(firstTagResult):
    for article in firstTagResult:
        username = article.find("span",{"class":"username"})
        content = article.find("p")
        if username is not None and content is not None:
            if  "abone" in content.text.lower():
                usernames.append(username)
                usernamee.add(username.text)
                print(username.text + "; " + content.text)
                print("")


print(websiteUrl)
soup = parseHTML(getHTML(websiteUrl))
isHtmlContentNeed = input("do you want to see full html content? y/yes or any key :")

if isHtmlContentNeed in ['yes','y','hell yeah']:
    isHtmlContentNeed = True
    if isHtmlContentNeed is True:
        print(soup)
else:
    print("skipping.")
    print("skipping..")
    isHtmlContentNeed = False
# elif isHtmlContentNeed.lower in ['no','n']:
#     isHtmlContentNeed = False

firstHtmlTag = input("First tag class you want to get: ") 
if firstHtmlTag == "":
    print("*** you missed the point where you should write something and default value is writed ***")
    firstHtmlTag = "article"
    
secondHtmlTag = input("second tag class you want to get: ") 
if secondHtmlTag == "":
    print("*** you missed the point where you should write something and default value is writed ***")
    # secondHtmlTag = "complaint-title"
    secondHtmlTag = "h2"

firstTagResult = getFirstTag(soup)

if firstTagResult is not None:
    startDrawing(firstTagResult)
    getCounts(firstTagResult)
    titles = getTitles(soup)
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
