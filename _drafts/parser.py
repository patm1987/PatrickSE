#!/usr/bin/python
import xml.etree.ElementTree as ET
import dateparser
import datetime

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
                pubDate = dateparser.parse(item.text)
                print('\tDate:', pubDate)
            if item.tag == '{http://wordpress.org/export/1.2/}post_id':
                print('\tPostID:', item.text)
            if item.tag == '{http://purl.org/rss/1.0/modules/content/}encoded':
                print('\tContent:', item.text)

class Page:
    '''
    Represents a single page from my old wordpress site
    '''
    def __init__(self):
        self.__title = None
        self.__date = None
        self.__post_id = None
        self.__content = None

    def set_title(self, title: str):
        '''
        Changes the title of the page
        Args:
            title (str): the new title of the page
        '''
        self.__title = title

    def set_date(self, date: datetime.datetime):
        '''
        Changes the date of the post
        Args:
            date (datetime.datetime): The date the page was created
        '''
        self.__date = date

    def set_post_id(self, post_id: str):
        '''
        Changes the id of the post. This is probably unecessary in our new framework
        Args:
            post_id (str): the id of this post
        '''
        self.__post_id = post_id

    def set_content(self, content: str):
        '''
        Sets the body of the post itself
        Args:
            constent (str): the body/content of the post
        '''
        self.__content = content
        