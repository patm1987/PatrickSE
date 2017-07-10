#!/usr/bin/python
import xml.etree.ElementTree as ET
import dateparser
from page import Page

tree = ET.parse('patrickse.wordpress.2017-06-20.xml')
print(tree.getroot())
channel = tree.getroot()[0]
for elem in channel:
    if elem.tag == 'item':
        page = Page()
        for item in elem:
            # print('\t', item)
            if item.tag == 'title':
                # print('\tTitle:', item.text)
                page.set_title(item.text)
            if item.tag == 'pubDate':
                pubDate = dateparser.parse(item.text)
                page.set_date(pubDate)
                # print('\tDate:', pubDate)
            if item.tag == '{http://wordpress.org/export/1.2/}post_id':
                page.set_post_id(item.text)
                # print('\tPostID:', item.text)
            if item.tag == '{http://purl.org/rss/1.0/modules/content/}encoded':
                page.set_content(item.text)
                # print('\tContent:', item.text)
        if page.can_write():
            print('Writing {}'.format(page.file_name()))
