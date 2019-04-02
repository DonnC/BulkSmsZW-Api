# handle sending messages using bulksmszw api
# obtain authentication details from http://portal.bulksmsweb.com

import requests
import logging
from BulkSmsApi.Parse import Parse

class Client:
    """
        client to connect to bulksms zw gateway and send a text message
    """

    __BULKSMS_WEBSERVICE_URL = "http://portal.bulksmsweb.com/index.php?app=ws"
    __SEND_SMS_OPERATION     = "pv"
    __SMS_CREDIT_OPERATION   = "cr"
    __STATUS_ERROR           = "ERR"
    
    def __init__(self, username=None, token=None):
        self.username = username
        self.token    = token
        logging.basicConfig(level="INFO")

    def __txt_op(self):
        # return url with username and token for text operation only
        if self.username and self.token:
            txt_op_details = "&u={user}&h={key}&op={operation}".format(
                user=self.username,
                key=self.token, 
                operation=self.__SEND_SMS_OPERATION)
            
            web_service_string = self.__BULKSMS_WEBSERVICE_URL + txt_op_details
            
            return web_service_string

        else:
            raise Exception("Username and Token not provided")

    def __credit(self):
        # url for credit retrieval
        if self.username and self.token:
            credit_details = "&u={user}&h={key}&op={operation}".format(
                user=self.username,
                key =self.token, 
                operation=self.__SMS_CREDIT_OPERATION)
            
            web_service_string = self.__BULKSMS_WEBSERVICE_URL + credit_details
            
            return web_service_string

        else:
            raise Exception("Username or Token not provided")


    def recipients(self, recipients_list):
        '''
            receive phone numbers as a list
            list is parsed and recipients numbers are extracted. Returns a string of phone numbers
        '''
        # TODO: Validate phone number format

        recipients = ""

        if type(recipients_list) == list:
            # recipients should be a list
            for phone_numbers in recipients_list:
                recipients += phone_numbers + ","

            recipients = recipients.rstrip(',')

            return recipients

        else:
            raise Exception("Recipients should be passed as a list")

    def __api_errors(self, error_response):
        # handle bulksmszw api error

        if error_response.get("status") == self.__STATUS_ERROR:
            # if status is in root node, and is has value 'ERR', there have been an exception
            return True

        elif error_response.get("data"):
            # 'data' values signifies text has been send correctly
            return False

    def send_request(self, text, to, operation):
        '''
            parse and quote phone numbers and the message body
            handles http post request to send text message use BulkSmsZw gateway
            BulkSmsZw status error codes are catched as Exceptions
        '''
        url = Parse(operation, text, to).url()

        req = requests.post(url)
        
        # check for error
        req.raise_for_status()

        response = req.json()
        
        if self.__api_errors(error_response=response):
            raise Exception(response)
 
        return response

    def send(self, body, recipients, credits=False, schedule=None):
        '''
            send message to recipients, phone_numbers are passed as a list of numbers or groups or mixed
            >>> send(body="Hello World", body=['#developer', '263778060126'])
            'credits' flag is set to True in order to return text messages left. Is set to False by default
            >>> send(body="Hello World", body=['#developer', '263778060126'], credits=True)
            on successful, it returns json body. If 'credits' is set to True, returns the credits value
        '''
        #TODO: Handle scheduling text message: YYYY-MM-DD hh:mm:ss

        recipients = self.recipients(recipients_list=recipients) 
        body       = body + "\n"                                                                    # for default sender ID
        
        if credits:
            resp = self.send_request(text=body, to=recipients, operation=self.__credit())
            
        else:
            resp = self.send_request(text=body, to=recipients, operation=self.__txt_op())

        return resp