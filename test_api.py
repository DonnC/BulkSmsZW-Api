#! Python
# testing the api

from BulkSmsApi import Client
from credentials import BULKSMS_NAME, BULKSMSWEB_KEY

print('API TESTING')

# provide credentials here
bulksms = Client(username=BULKSMS_NAME, token=BULKSMSWEB_KEY)

# try sending
try:
    # set "credit" flag = True so as to get text sms left on your web portal
    print("Sending..")
    resp = bulksms.send(body="hello, bulksmszw api test run", recipients=['2637xxxxxxxx'], credits=True)
    print(resp)

except Exception as exc:
    print("Error: %s" % exc)
