from pamsdkpython import ShiftechAPI
api = ShiftechAPI()

#requires token to operate
def RequestVALIDATION():
    try:
        response = api.PaybillTillNumbers()
        return response
    except Exception as e:
        print(f'{e}')
def GetTOKEN():
    try:
        response = api.RequestToken()
        return response
    except Exception as e:
        pass    

def Apps():
    try:
        response = api.RequestApps()
        return response
    except Exception as e:pass 

def Transactions():
    try:
        response = api.RequestTransactions()
        return response
    except Exception as e:pass

def   C2BRegistersUrl():
    try:
        response = api.C2BRegister() 
        return response
    except Exception as e:pass

def    pushSTK():
    try:
        response = api.stkpush()
        return response
    except Exception as e:pass

def   Paybulk():
    try:
        response = api.BulkPayments()
        return response
    except Exception as e:pass     

def  checkbalance():
    try:
        response = api.balance()
        return response
    except Exception as e:pass

def confirmpayments():
    try:
        response = api.ConfirmStkPayment()
        return response
    except Exception as e:pass

def confirmwithdrwal():
        try:
            response = api.ConfirmWithdraw()
            return response
        except Exception as e:pass
    


if  __name__ == "__main__":
    
    print(f".................shiftechafrica.com..........................")
    print(f"..............PAYMENT ACCOUNT MANAGEMENT.................... ")
    print(f"...............PAM API CLIENT V 1.O..........................")
    print(f"..........SELECT ACTIONS TO PERFORM ON PAYMENT...............")
    print(f".............................................................")

    print(f"[1] REQUEST BEARER TOKEN ")
    print(f"[2] VALIDATE")
    print(f"[3] APPLICATIONS")
    print(f"[4] TRANSACTIONS")
    print(f"[5] CB2 REGISTER")
    print(f"[6] STK PUSH")
    print(f"[7] BULK PAYMENTS")
    print(f"[8] CHECK BALANCE")
    print(f"[9] CONFIRM STK PAYMENTS")
    print(f"[10] CONFIRM WIDTHDRAWALS")

    selection = input("ENTER ANY OF ABOVE ACTIONS TO OPERATE:")

    if selection == 1:
        GetTOKEN()
    elif selection == 2:
        RequestVALIDATION()
    elif selection == 3:
        Apps()
    elif selection == 4:
        Transactions()
    elif selection == 5:
        C2BRegistersUrl()
    elif selection == 6:
        pushSTK()
    elif selection == 7:
        Paybulk()
    elif selection == 8:
        checkbalance()
    elif selection == 9:
        confirmpayments()
    elif selection == 10:
        confirmwithdrwal()
    else:
        print(f"INVALID SELECTION,RETRY AGAIN")    
