import json
import requests

# beartoken = "ENTER BEAR TOKEN HERE IT EXPIRES AFTER 3600 SECONDS"
consumerkey = str.format('ENTER THE CONSUMER KEY')
consumersecret = str.format('ENTER THE CONSUMER SECRET')
c2b_secret = str.format('ENTER THE C2B SECRET')
token = str.format('ENTER HERE')
beartoken = str.format('ENTER THE GENERATED BEAR TOKEN EXPIRES WITHIN 3600 UNIT OF TIME')
secret = str.format('ENTER SECRET HERE')


class ShiftechAPI:
    def __init__(self, base=0, token=0):
        self.base = 'https://pam.api.easyncpay.com/api/v1'
        self.token = f'{token}'

    def RequestToken(self):
        url = "https://pam.api.easyncpay.com/api/v1/token?Content-Type=application/json&Accept=application/json&Authorization=Basic {token}"

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Basic {token}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.json())

    def PaybillTillNumbers(self):
        url = "https://pam.api.easyncpay.com/api/v1/shortcode/m-pesa/shortcode/validate?Content-Type=application/json&Accept=application/json&Authorization=Bearer {beartoken}"

        payload = json.dumps({
            "ConsumerKey": f"{consumerkey}",
            "ConsumerSecret": f"{consumersecret}",
            "Environment": "sandbox"
        })
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {beartoken}"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.json())

    def RequestApps(self):
        url = "https://pam.api.easyncpay.com/api/v1/app/?Accept=application/json"

        payload = {}
        headers = {
            'Accept': 'application/json',
            'Authorization': f"Bearer {beartoken}"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.json())

    def RequestTransactions(self):
        url = "https://pam.api.easyncpay.com/api/v1/pay-loads?Accept=application/json"

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {beartoken}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.json())

    def C2BRegister(self):
        url = "https://pam.api.easyncpay.com/api/v1/m-pesa/c2b/register-url?Content-Type=application/json&Accept=application/json&Authorization=Bearer {beartoken}"

        payload = json.dumps({
            "Secret": f'{secret}'
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {beartoken}'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.json())

    def stkpush(self):
        url = "https://pam.api.easyncpay.com/api/v1/m-pesa/c2b/stk-push?Accept=application/json&Content-Type=application/json&Authorization=Bearer {beartoken}"

        payload = json.dumps({
            "CallingCode": "254",
            "Secret": f"{c2b_secret}",
            "PhoneNumber": "0713255791",
            "Amount": 1,
            "ResultUrl": "https://pam.easyncpay.com/api/callbacks/confirm",
            "Description": "Testing the PAM API",
            "TransactionType": "CustomerPayBillOnline"
        })
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {beartoken}'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.json())

    def BulkPayments(self):
        url = "https://pam.api.easyncpay.com/api/v1/m-pesa/b2c?Content-Type=application/json&Accept=application/json&Authorization=Bearer {beartoken}"

        payload = json.dumps({
            "CallingCode": "254",
            "Secret": f"{secret}",
            "PhoneNumber": "0713255791",
            "Amount": 7000,
            "ResultUrl": "https://pam.easyncpay.com/api/callbacks/withdraw",
            "Description": "Office Water....",
            "TransactionType": "BusinessPayment"
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {beartoken}'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.json())

    def balance(self):
        url = "https://pam.api.easyncpay.com/api/v1/m-pesa/shortcode/balance?Content-Type=application/json&Accept=application/json&Authorization=Bearer {beartoken}"

        payload = json.dumps({
            "Secret": f"{secret}"
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {beartoken}'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.json())

    def ConfirmStkPayment(self):
        url = "https://pam.api.easyncpay.com/api/v1/m-pesa/c2b/confirm-stk-payment?Accept=application/json&Content-Type=application/json&Authorization=Bearer {beartoken}"

        payload = json.dumps({
            "Secret": f"{c2b_secret}",
            "ReferenceNumber": "3ELBTYUBSE",
            "ResultUrl": "https://webhook.site/2ca81704-747e-492f-833b-c8d5cb13a2b3"
        })
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {beartoken} '
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.json())

    def ConfirmWithdraw(self):
        url = "https://pam.api.easyncpay.com/api/v1/m-pesa/b2c/confirm-withdraw?Accept=application/json&Content-Type=application/json&Authorization=Bearer {beartoken}"

        payload = json.dumps({
            "Secret": f"{secret}",
            "ReferenceNumber": "2G6MPL7EQB",
            "ResultUrl": "https://pam.easyncpay.com/api/callbacks/confirm"
        })
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {beartoken}'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()
