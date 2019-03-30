# testing the api

from BulkSmsApi import Client

BULKSMS_NAME   = "<your-username>"
BULKSMSWEB_KEY = "<webservice-token>"

# provide credentials here
bulksms = Client(username=BULKSMS_NAME, token=BULKSMSWEB_KEY)

# try sending
try:
    # set "credit" flag = True so as to get text sms left on your web portal
    print("Sending..")
    resp = bulksms.send(body="hello world. Api test run", recipients=['2637xxxxxxxx'], credits=True)
    print(resp)

except Exception as exc:
    print("Error: %s" % exc)
