#! Python
# testing the api

from BulkSmsApi import Client
from credentials import BULKSMS_NAME, BULKSMSWEB_KEY

print('API TESTING')

# provide credentials here
bulksms = Client(username=BULKSMS_NAME, token=BULKSMSWEB_KEY)

# try sending
try:
    print("Sending..")
    resp = bulksms.send(body="hello, api test 2", recipients=['263782897884'], credits=True)
    print(resp)

except Exception as exc:
    print("Error: %s" %exc)