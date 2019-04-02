# handle url encoding
# do 'quote' on url

from urllib.parse import quote

class Parse(object):
    '''
        parse and encode webservice payload
    '''
    def __init__(self, web_url, quote_body, quote_recipients):
        self.web_url          = web_url
        self.quote_body       = quote_body
        self.quote_recipients = quote_recipients

    def url(self):
        return self.web_url + self.__payload()

    def __body(self):
        '''quote body of text '''
        return quote(self.quote_body)

    def __recipients(self):
        '''quote recipients list'''
        return quote(self.quote_recipients)

    def __payload(self):
        '''return payload'''
        url_payload = ""
        url_payload += "&to=" + self.__recipients()
        url_payload += "&msg=" + self.__body()

        return url_payload