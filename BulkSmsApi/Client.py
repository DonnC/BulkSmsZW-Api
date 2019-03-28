# handle sending messages using bulksmszw api
# obtain authentication details from http://portal.bulksmsweb.com

import requests
import logging

class Client:
    """
        - client to connect to bulksms and send a message
        - by default a general text message is send
        - to retrieve credits, the flag "credits" is set to true. False by default
        - recipients to send message to is passed in as a list of numbers/groups or mixed
        - messages can be scheduled with bulksms supported datetime format: YYYY-MM-DD hh:mm:ss
    """

    BULKSMS_WEBSERVICE_URL = "http://portal.bulksmsweb.com/index.php?app=ws"
    SEND_SMS_OPERATION     = "pv"
    SMS_CREDIT_OPERATION   = "cr"
   
    __name__    = "BulkSmsZW API"
    __author__  = "Donald C"
    __version__ = 1.0

    def __init__(self, username=None, token=None):
        self.username = username
        self.token    = token
        logging.basicConfig(level="INFO")

    def txt_op(self):
        # return url with username and token for text operation only
        if self.username and self.token:
            txt_op_details = "&u={user}&={key}&op={operation}".format(
                user=self.username,
                key=self.token, 
                operation=self.SEND_SMS_OPERATION)
            
            web_service_string = self.BULKSMS_WEBSERVICE_URL + txt_op_details
            
            return web_service_string

        else:
            raise Exception("Username and Token not provided")

    def credit(self):
        # url for credit retrieval
        if self.username and self.token:
            credit_details = "&u={user}&h={key}&op={operation}".format(
                user=self.username,
                key =self.token, 
                operation=self.SMS_CREDIT_OPERATION)
            
            web_service_string = self.BULKSMS_WEBSERVICE_URL + credit_details
            
            return web_service_string

        else:
            raise Exception("Username or Token not provided")


    def recipients(self, recipients_list):
        # receive recipient as lists
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

    def send_request(self, text, to, operation):
        payload = dict()
        payload["to"] = to
        payload["msg"] = text

        req = requests.post(operation, data=payload)

        try:
            req.raise_for_status()
            response = req.json()
            return response

        except Exception as error:
            print("There was an error sending text request: %s" %error)
            return error

    def send(self, body, recipients, credits=False, schedule=None):
        #TODO: Handle scheduling text message: YYYY-MM-DD hh:mm:ss
        #TODO: Retrieve user credits

        recipients = self.recipients(recipients_list=recipients)
        
        if credits:
            resp = self.send_request(text=body, to=recipients, operation=self.credit())
            
        else:
            resp = self.send_request(text=body, to=recipients, operation=self.txt_op())

        return resp