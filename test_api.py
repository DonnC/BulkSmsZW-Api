# testing the api
from BulkSmsApi.Client import Client

BULKSMS_NAME   = "<your-username>"
BULKSMSWEB_KEY = "<webservice-token>"

# provide credentials here
bulksms         = Client(username=BULKSMS_NAME, token=BULKSMSWEB_KEY)

message         = "Bulksms api test successful"
phone_numbers   = ['2637xxxxxxxx', '2637yyyyyyyy', '#devteam']

try:
    resp = bulksms.send(message, phone_numbers)
    print(resp)

except Exception as exc:
    print("Encountered an Error: %s" %exc)
