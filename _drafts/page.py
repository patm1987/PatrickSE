import datetime

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

    def can_write(self) -> bool:
        '''
        Returns true if everything is set to true
        '''
        if self.__title is not None:
            if self.__date is not None:
                if self.__post_id is not None:
                    if self.__content is not None:
                        return True
        return False

    def file_name(self) -> str:
        '''
        Gets the filename to write out
        '''
        date = self.__date
        return '{}-{}-{}-{}.md'.format(date.year, date.month, date.day, self.__title)
