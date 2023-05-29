# <p align="center"><a href="https://pam.easyncpay.com" target="_blank"><img width="200" src="https://pam.easyncpay.com/img/logo.png"></a></p>

<p align="center">
  <b>Python Paybill Acount Manager</b><br>
  
  <br><br>
  <a href="https://pam.easyncpay.com/docs"><img src="https://github.com/dev-techguy/TechGuy/blob/master/doc.png" width="200"></a>
</p>

## Introduction

This library handles all the PAM - PayBill Account Manager API's,that are then linked to Safaricom M-pesa Portals.

## Installing

The recommended way to install pam-php-sdk is through
[Git](https://git-scm.com).

```bash
# Install package via git clone
git clone https://github.com/SHIFTECH-AFRICA/pam-python-sdk.git

```

Next, install the modules inside requirements.txt with pip:

```bash
# install modules
 cd pam-python-sdk
 pip install -r requirements.txt
```

After installing, the library set relevant api variables:

```python
# this parts need to be filled for easy operation with API
consumerkey = str.format('ENTER THE CONSUMER KEY')
consumersecret = str.format('ENTER THE CONSUMER SECRET')
c2b_secret = str.format('ENTER THE C2B SECRET')
token = str.format('ENTER HERE')
beartoken = str.format('ENTER THE GENERATED BEAR TOKEN EXPIRES WITHIN 3600 UNIT OF TIME')
secret = str.format('ENTER B2C SECRET HERE')
```

## Usage

Follow the steps below on how to use the pam-python-sdk:

#### How to use the Library

How to use the pam-python-sdk to initiate different levels of *api's*

```python
       
from pampythonsdk.pampythonsdk import ShiftechAPI

api = ShiftechAPI()

"""
    REQUEST FOR A BEARER TOKEN FOR AUTHORIZATION THE API FUNCTIONS NEED TO BE AUTHORISED
"""
def GetTOKEN():
    try:
        response = api.RequestToken()
        return response
    except Exception as e:
        pass
"""
	Validating PayBill/Till Number
	Provide all the valid information to check if the paybill/till number 
	credentials are valid.	
"""
def RequestVALIDATION():
    try:
        response = api.PaybillTillNumbers()
        return response
    except Exception as e:
        print(f'{e}')

"""
	Apps
	Listing all your apps.
"""
def Apps():
    try:
        response = api.RequestApps()
        return response
    except Exception as e:
        pass
"""
	Register C2B Callback
	Here register the confirm and validation url.
"""
def C2BRegistersUrl():
    try:
        response = api.C2BRegister()
        return response
    except Exception as e:
        pass
"""
	STK PUSH
	This section shows how to make stk push and callback data for both stk-push
 	and lipa na mpesa.	
"""
def pushSTK():
    try:
        response = api.stkpush()
        return response
    except Exception as e:
        pass

"""
    BALANCE
    This section shows you how to query the balance
"""
def checkbalance():
    try:
        response = api.balance()
        return response
    except Exception as e:
        pass
"""
    B2C
    This is where all the bulk payments are made.
"""
def Paybulk():
    try:
        response = api.BulkPayments()
        return response
    except Exception as e:
        pass
"""
    CONFIRM BULK PAYMENTS
    This is where the confirmation for stk payments are made
"""
def confirmpayments():
    try:
        response = api.ConfirmStkPayment()
        return response
    except Exception as e:
        pass
"""
    WITHDRAWAL CONFIRMATIONS
    This is where the confirmation for withdrawals are made
"""    
def confirmwithdrwal():
    try:
        response = api.ConfirmWithdraw()
        return response
    except Exception as e:
        pass


```

## API Responses

These are the responses that one expects from each api requests.

### PayBill/ShortCode Credentials Validation

```python

   # Sample 200 response
    "data": {
        "Message": "The m-pesa app keys are valid."
    },
    "success": true

```

### Register C2B URL (confirm/validation)

```python

     # Sample 200 response
    "data": {
        "Message": "Validation and Confirmation URLs are already registered"
    },
    "success": true

```

### Balance Response

```python

     # Sample 200 response
    "data": {
        "Number": XXXXX,
        "Balance": 38,000.00
    },
    "success": true

```

### STK-PUSH/C2B LIPA NA M-PESA

```python

    # This the response for making a successful request
    "data": {
        "Message": "Request accepted for processing...",
        "ReferenceNumber": "2BONOSBBTN"
    }
    "success": true

    # stk successful payment done.
    "data": {
        "Success": true,
        "Description": "The service request is processed successfully.",
        "ReferenceNumber": "2BONOSBBTN",
        "PhoneNumber": "254XXXXXXXXX",
        "MpesaReceiptNumber": "PBO2ZOBY44",
        "Amount": 20000
    }

    # c2b/lipa na mpesa successful payment done.
    "data": {
        "Success": true,
        "Description": "The service request is processed successfully.",
        "ReferenceNumber": "2BONOSBBTN",
        "PhoneNumber": "254XXXXXXXXX",
        "MpesaReceiptNumber": "PBO2ZOBY44",
        "Amount": 20000,
        'TransactionType': 'Pay Bill'
        'OrgAccountBalance': 50000,
        'ShortCode':xxxxxx
    }

    # stk/c2b payment not done
    "data": {
        "Success": false,
        "Description": "Request cancelled by user",
        "ReferenceNumber": "2BOXRDNMLU",
        "PhoneNumber": "254XXXXXXXXX"
    }
    
    # This the response for checking stk push payment - similar to mpesa stk push query
    "data": {
        "Message": "Accepted for processing..."
    }
    "success": true
    
    # stk push payment confirmation callback...
    "data": {
        "Success": true or false,
        "Description": "The service request is processed successfully.",
        "ReferenceNumber": "2BONOSBBTN",
        "PhoneNumber": "254XXXXXXXXX",
        "MpesaReceiptNumber": "PBO2ZOBY44",
        "Amount": 20000
    }

```

### B2C/BULK PAYMENT

```python

    # This the response for making a successful request
    "data": {
        "Message": "Request accepted for processing...",
        "ReferenceNumber": "2BO6BCTLYF"
    },
    "success": true

    # b2c successful withdraw payment done.
    "data": {
       'Success' => true,
       'Description' => 'Salary payment',
       'ReferenceNumber' => '2BO6BCTLYF',
       'PhoneNumber' => '254XXXXXXXXX',
       'MpesaReceiptNumber' => 'PBO2ZOBY44',
       'Amount' => 50000,
       'B2CUtilityAccountAvailableFunds' => 70000,
       'B2CWorkingAccountAvailableFunds' => 70000,
       'B2CChargesPaidAccountAvailableFunds' => 70000
    }

    # b2c withdraw payment not done.
    "data": {
        "Success": false,
        "Description": "The initiator information is invalid.",
        "ReferenceNumber": "2BO6BCTLYF",
        "PhoneNumber": "254XXXXXXXXX"
    }   
     
    # This the response for checking withdrawal payment
    "data": {
        "Message": "Accepted for processing..."
    }
    "success": true
    
    # withdrawal payment confirmation callback...
    "data": {
       'Success' => true or false,
       'Description' => 'Salary payment',
       'ReferenceNumber' => '2BO6BCTLYF',
       'PhoneNumber' => '254XXXXXXXXX',
       'MpesaReceiptNumber' => 'PBO2ZOBY44',
       'Amount' => 50000,
       'B2CUtilityAccountAvailableFunds' => 70000,
       'B2CWorkingAccountAvailableFunds' => 70000,
       'B2CChargesPaidAccountAvailableFunds' => 70000
    }

```



[pam-php-sdk-repo]: https://github.com/SHIFTECH-AFRICA/pam-python-sdk.git

## Security Vulnerabilities

For any security vulnerabilities, please email to [Shiftech Africa](mailto:bugs@shiftech.co.ke).

## License

This package is open-source, licensed under the [GNU GENERAL PUBLIC LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html).
