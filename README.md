# [BulkSmsZW-Api](http://www.bulksmsweb.com/)
bulksmszw api for sending text messages

## Authentication details
- register an account on [bulksms website](http://www.bulksmsweb.com/)
- if already have an account, login on [bulksms web portal](http://portal.bulksmsweb.com) to obtain authentication details

## Sending default message
- check out [test file](https://github.com/DonnC/BulkSmsZW/test_api.py)
- recipients is passed as a list of bulksms valid format ```2637xxxxxxxx```, list can also contain groups ```#devteam``` and can be mixed
```python
api = Client(<username>, <token>)
api.send("hello guys", ['2637xxxxxxxx', '#devteam', '#students']
```
- Example script below
```python
from BulkSmsApi import Client

BULKSMS_NAME   = "your-username"
BULKSMSWEB_KEY = "your-web-token"

bulksms = Client(username=BULKSMS_NAME, token=BULKSMSWEB_KEY)

try:
    response = bulksms.send(body="bulk sms ZW api testing", recipients=['2637xxxxxxxx', '2637yyyyyyyy])
    print(response)

except Exception as exc:
    print("Error: %s" %exc)
```

## Send message and get credits left
- ```credits``` flag by default is set to ```False```
- to send a message and receive the number of credits left on your web portal, set the ```credit=True``` flag

## Responses
- responses are in default **JSON** format used by BulkSMSZW service

## acknowledgements
- i would like to greatly extend my gratitude to the BulkSMS ZW team
- the default [python script](http://portal.bulksmsweb.com/sample/samplepy.html) they provided is the one i just took the opportunity to extend
- i give all credits to the Bulk SMS Team

## HTTP API
- more information is found at [HTTP API INTEGRATION DOC](http://portal.bulksmsweb.com/downloads/BulkSMS-API.pdf)

## [TODO]()
- Schedule messages
