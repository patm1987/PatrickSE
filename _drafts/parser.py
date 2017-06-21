#!/usr/bin/python
import xml.etree.ElementTree as ET
tree = ET.parse('patrickse.wordpress.2017-06-20.xml')
print(tree.getroot())
channel = tree.getroot()[0]
for elem in channel:
    print(elem)
    if elem.tag == 'item':
        for item in elem:
            # print('\t', item)
            if item.tag == 'title':
                print('\tTitle:', item.text)
            if item.tag == 'pubDate':
                print('\tDate:', item.text)
            if item.tag == '{http://wordpress.org/export/1.2/}post_id':
                print('\tPostID:', item.text)
            if item.tag == '{http://purl.org/rss/1.0/modules/content/}encoded':
                print('\tContent:', item.text)
