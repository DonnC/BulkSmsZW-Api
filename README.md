# [BulkSmsZW-Api](http://www.bulksmsweb.com/)
- bulksmszw api for sending affordable text messages

# Installation
- make sure git is installed on your system or download repo as zip
- In **cmd** or **terminal** do

```bash
$ git clone https://github.com/DonnC/BulkSmsZW-Api.git
$ cd BulkSmsZW-Api
$ python setup.py install
```

## Authentication details
- register an account on [bulksms website](http://www.bulksmsweb.com/)
- if already have an account, login on [bulksms web portal](http://portal.bulksmsweb.com)
- Got to "My Account", then Click on "User Configuration", to obtain "Webservices token".

## Sending default message
- test file [test_api.py](https://github.com/DonnC/BulkSmsZW-Api/blob/master/test_api.py)
- recipients is passed as a list of bulksms valid format ```2637xxxxxxxx```, list can also contain groups ```#devteam``` and can be mixed

```python
 api = Client(<username>, <token>)
 respond = api.send("hello guys", ['2637xxxxxxxx', '#devteam', '#students'])
```

- Example script

```python
from BulkSmsApi import Client

BULKSMS_NAME   = "your-username"
BULKSMSWEB_KEY = "your-web-token"

bulksms = Client(username=BULKSMS_NAME, token=BULKSMSWEB_KEY)

try:
    response = bulksms.send(body="bulk sms ZW api testing", recipients=['2637xxxxxxxx', '2637yyyyyyyy'])
    print(response)

except Exception as exc:
    print("Encountered an Error: %s" %exc)
```

## Send message and get credits(text messages) left
- ```credits``` flag by default is set to ```False```
- to send a message and receive the number of credits left on your web portal, set the ```credit``` flag to ```True```

```python
api = Client(<username>, <token>)
credits_response = api.send(body="hello world", recipients=['2637xxxxxxxx'], credits=True)
print(credits_response)
```

## Responses
- responses are in default **JSON** format used by BulkSMSZW service

## acknowledgements
- Big shoutout to the BulkSMS ZW team
- Original bulksms [python api script](http://portal.bulksmsweb.com/sample/samplepy.html)
- All credits to the Bulk SMS ZW Team

## HTTP API
- api docs [HTTP API INTEGRATION DOC](http://portal.bulksmsweb.com/downloads/BulkSMS-API.pdf)

## [TODO]()
- Schedule messages
- Validate phone numbers

## dev
- [twitter](https://twitter.com/@donix_22)
