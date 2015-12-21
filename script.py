import config
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
import os
import requests
import twitter

api = twitter.Api(consumer_key=config.consumer_key,
                  consumer_secret=config.consumer_secret,
                  access_token_key=config.access_token_key,
                  access_token_secret=config.access_token_secret)

# open the webpage
driver = webdriver.Firefox()
driver.get("https://facebook.com/hashtag/" + config.hashtag)

# get the names and statuses using xpath
names = driver.find_elements_by_xpath('//*[@class="fwb fcg"]')
statuses = driver.find_elements_by_xpath('//*[@class="_5pbx userContent"]')

# create the file containing previously processed names/statuses (if it doesn't already exist)
if not os.path.exists(config.filename):
    file(config.filename, 'w').close()

# open the file 
myfile = open(config.filename, "r")
current = myfile.read()
myfile.close()

# get index of all names in this file (hopefully nobody's name contains 'xzyx.')
namesList = [m.start() for m in re.finditer('xzyx.', current)]

# open the same file for writing any new names
myfile = open(config.filename, "a")
myfile.write(str("\n"))

# for each name retrieved
for i in range(0, len(names)):
  name = str(names[i].text.encode('ascii', 'ignore'))
  status = str(statuses[i].text.encode('ascii', 'ignore'))

  mainBreak = False

  # check each previously written name
  for nn in namesList:
    loop = 0
    for ni in range(0, len(name)):
      # check by matching characters of the name one by one
      if name[ni] == current[(nn+5)+ni]:
        loop = loop + 1

    if loop == len(name):
      mainBreak = True
      break

  # if name already written then skip processing for this post
  if mainBreak:
    continue

  myfile.write(str('xzyx.'))
  myfile.write(name)
  myfile.write(str('\n'))
  myfile.write(status)
  myfile.write(str("\n--------------\n"))

  # post status to twitter!
  msg = str(name + '\n' + status)
  # truncate to 139 characters
  msg1 = (msg[:136] + '...') if len(msg) > 136 else msg
  status = api.PostUpdate(msg1)
  print status
  print msg1

myfile.write(str("\n********************\n"))
driver.quit()
myfile.close()
