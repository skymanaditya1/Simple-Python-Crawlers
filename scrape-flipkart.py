from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import requests
import wget
titles = []

titles1 = []
url_name = "https://www.flipkart.com/search?q="
query = "laptop"
link = url_name + query
driver = webdriver.Firefox()
driver.get(link)
##page = driver.text # loads the entire page in the page 
##soup = BeautifulSoup(page)
##print(soup.prettify)
elems = driver.find_elements_by_tag_name("a")
for elem in elems:
   if(elem.get_attribute("class") == "fk-display-block"):
      titles.append(elem.get_attribute("title"))
   '''   
elems1 = driver.find_elements_by_tag_name("a")
for elem1 in elems1:
   if(elem1.get_attribute("class") == "rating"):
      titles1.append(elemt1.get_attribute("style"))
   '''
'''hello = driver.find_element_by_tag_name("body")
elem = hello.get_attribute("class") # prints out browse new-branding
hello1 = hello.find_element_by_class_name("

print(elem)'''
'''for elem in hello:
   if(elem.get_attribute("class") == "newMenu  fkart fksk-body line  "):
   hello1 = elem.   
   '''   
   
print(titles)
print(titles[0]) # Check for the first item in the titles list'''
file_name = '/home/aditya/flipkart-input'
f = open(file_name, 'w')
for item in titles:
   f.write(item)
f.close()
driver.close()
