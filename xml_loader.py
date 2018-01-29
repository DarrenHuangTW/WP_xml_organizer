# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:54:39 2018

@author: Darren Huang
"""

# =============================================================================
# Organize the posts XML data downloaded from Wordpress and output an clean csv file 
# =============================================================================

from bs4 import BeautifulSoup
import csv

xml = open('prophet.wordpress.2018-01-24.xml','r', encoding="utf-8")

posts_data=[]

soup = BeautifulSoup(xml, 'xml')
items = soup.rss.channel.findAll("item")

for post in items:
    title = post.title.string
    link = post.link.string
    pubDate = post.pubDate.string
    arthur = post.creator.string
    category = post.find('category',domain='category').string
    posts_data.append([title, link, pubDate, arthur, category])


field = ["Title", "Link", "Published Date", "Arthur", "Category"]

with open('post-data.csv', 'w', encoding="utf-8", newline='\n') as file:
    writer = csv.writer(file)
    writer.writerow(field)
    for row in posts_data:
        writer.writerow(row)

xml.close()