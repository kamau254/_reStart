#!/usr/bin/env python

import json
import getpass
import random
import datetime
now = datetime.datetime.now()

#Database of user accounts
records = []

def parse(d):
    
    dictionary = dict()
    # Removes curly braces and splits the pairs into a list
    pairs = d.strip('{}').split(', ')
    for i in pairs:
        pair = i.split(': ')
        # Other symbols from the key-value pair should be stripped.
        dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
    return dictionary
try:
    file = open('atm.csv', 'rt')
    lines = file.read().split('\n')
    for l in lines:
        if l != '':
            dictionary = parse(l)
            records.append(dictionary)
    file.close()  
except:
    print("Something unexpected occurred!")

userArray = records   

# create_user() 
def create_user():
    username = input('Enter your username: ')
    with open('atm.csv', 'r+') as f:
        user = f.read()
        f.close()
        if username in user: 
            print("The user exist in our databases")
        else:
            with open('atm.csv', 'a+') as file:
                pin = getpass.getpass('Enter your pin: ')
                ksh = int(input('Enter amount in KSH: '))
                usd = int(input('Enter amount in USD: '))
                users = {'username':username, 'pin': pin, 'balance': ksh}
                file.write('\n' + json.dumps(users))      
                print('ACCOUNT SUCCESSFULLY CREATED') 

# ATM TRANSACTION 
def transact():
    # Main Interaction Menu after Successful LogIn       
    def atmMenu():

        # DISPLAY WELCOME MESSAGE
        print (('\nGamma International Banking System\n \n       Please follow the instructions for a successful transaction').upper())
        print ('\nPlease enter your credentials to login\n \n')
        print (f"\nWelcome " + str( username.upper()) + "\n \nWhat would you like to do today? \n")
        
        # CHECK USER TRANSACTION SELECTION
        while True:
            # REQUEST USER TRANSACTION SELECTION
            print ("Type the number associated with the transaction you want to perform and \nPress enter to select")
                 
            try:
                transaction = int(input("1) Check Balance  2) Make Withdrawal  3) Mobile Money  4) Change Pin 5) Quit / Log Out\n \n"))

                # CHECK IF USER WANTS TO CHECK BALANCE AND RUN
                if transaction == 1:
                    # RUN THE BALANCE CHECK FUNCTION
                    crntBalance()
                    pause = input('Press Enter to return to the Main Menu ')
                     
                    continue
                    
                # CHECK IF USER WANTS TO MAKE A WITHDRAWAL AND RUN
                elif transaction == 2:
                    # RUN THE WITHDRAWAL FUNCTION AND SAVE ALL OUTPUTS TO THE VARIABLE
                    withdrawn = withdrawUpdate()
                    # RUN THE RECEIPT REQUEST FUNCTION
                    rcptPrint(withdrawn)
                    break
                
                # CHECK IF USER WANTS TO MAKE A MOBILE MONEY WITHDRAWAL
                elif transaction == 3:
                    # RUN THE MOBILE MONEY FUNCTION
                    pesa()
                    break
                
                # CHECK IF USER WANTS TO UPDATE PIN
                elif transaction == 4:
                     # RUN THE UPDATE PIN FUNCTION
                    updatePin()
                    break
                
                # CHECK IF USER WANTS QUIT OR LOG OFF
                elif transaction == 5:
                    while True:
                        # REQUEST INPUT FROM USER
                         
                        quitConfirm = str(input('Are you sure you want to quit? (Y/N):  ')).upper()
                         
                        # IF USER SAYS YES END PROGRAM
                        if quitConfirm == 'Y':
                            print('''            
                                        ---------------------------------------------------------------------------------------
                                        *                      Thank You For Banking With Us.                                  *        
                                        *                         Gamma International Bank                                     *    
                                        *                We don't except a big deposit, but small deposits add up.             *     
                                        ----------------------------------------------------------------------------------------''')
                            exit()

                        # IF USER SAYS NO RELOAD THE MAIN MENU
                        elif quitConfirm == 'N':
                            break
                        
                        # IF USER RESPONSE IS INVALID ASK FOR A VALID INPUT
                        else:
                            print ('Invalid input. Try again')
                            continue
                    continue
                else:
                    print ('Invalid selection input. Try again')
                    continue
            except ValueError:
                print ('Invalid selection input. Please input a whole number')
                continue

        # CHECK IF USER WOULD LIKE TO PERFORM ANOTHER TRANSACTION
        while True:
            # REQUEST INPUT FROM USER
            backtoMain = str(input('Would you like to perform another another transaction? Y/N :  ')).upper()
            # IF USER SAYS YES RELOAD THE MAIN MENU
            if  backtoMain == 'Y':
                return atmMenu()
            # IF USER SAYS NO END PROGRAM
            elif  backtoMain == 'N':
                print('''            
                            ---------------------------------------------------------------------------------------
                            *                      Thank You For Banking With Us.                                  *        
                            *                         Gamma International Bank                                     *    
                            *                We don't except a big deposit, but small deposits add up.             *     
                            ----------------------------------------------------------------------------------------''')
                exit()
            # IF USER RESPONSE IS INVALID ASK FOR A VALID INPUT
            else:
                print ('        Invalid input. Try again')
                continue
            
    # WITHDRAWAL AND BALANCE UPDATE FUNCTION
    def withdrawUpdate():
        # DISPLAY FUNCTION MESSAGE
        print ('******************************************* ATM WITHDRAWAL*******************************************\n \n')
        print (('Gamma International Banking App\n \n Please follow the instructions for a successful transaction').upper())
        # SET A MINIMUM BALANCE LIMIT
        minimumBalance = 50
        # SET A MAXIMUM WITHDRAWAL LIMIT
        maxWithdrawal = 5000
        # TAKE USER INPUTS ON WITHDRAWAL SPECIFICS
        def withdrawRequest():
        # TAKE CURRENCY INPUT 
            while True:
                print ('******************************************* CURRENCY *******************************************\n \n')
                currency = str(input('      Withdraw from USD or KSH account (Type D for USD / K for KSH):\n').upper())
                # IF THE USER INPUT IS INCORRECT RESTART FUNCTION
                if currency not in ('D', 'K'):
                    print("         Invalid choice. Please try again")
                    continue
                
                # IF THE USER INPUT IS CORRECT ASSIGN THE SELECTED CURRENCY TO THE VARIABLE CURRENCY
                elif currency == 'D':
                    currency = 'USD'
                    break
                elif currency == 'K':
                    currency = 'KSH'
                    break
            
            # TAKE AMOUNT INPUT
            while True:
                print ('\n******************************************* AMOUNT *******************************************\n \n')
                # CHECK THE AMOUNT VALUE INPUTTED
                try:
                    amount = int(input('Please enter the amount you want to withdraw:\n'))
                    # IF THE WITHDRAWAL AMOUNT IS MORE THAN THE USERS BALANCE DO THIS
                    balance = int(session['balance'])
                    if amount >= balance:
                        # ALLOW USER TO DECIDE TO TR AGAIN OR RETURN TO MAIN MENU
                        while True:
                            stopContinue = str(input("Insufficient Funds\n \nWould you like to try again or return to the main Menu?\n \n Type 'Y' to try agin or Type 'N' to return to the main Menu:  ")).upper()
                            # IF THE USER INPUT IS INCORRECT ASK FOR CORRECT INPUT
                            if stopContinue not in ('Y', 'N'):
                                print ('Invalid Input, try again.')
                                continue
                            # IF USER SAYS YES RESTART FUNCTION AND TAKE CORRECT AMOUNT INPUT
                            elif stopContinue == 'Y':
                                break
                            # IF USER SAYS NO RETURN TO THE MAIN MENU
                            elif stopContinue == 'N':
                                return atmMenu()
                        continue
                    # IF THE WITHDRAWAL AMOUNT IS LESS THAN THE USERS BALANCE MOVE TO THE NEXT STEP
                    elif amount < balance:
                        # CHECK USER BALANCE AFTER SPECIFIED WITHDRAWAL AMOUNT IS WITHDRAWN
                        balanceAfterWithdraw = balance - amount
                        # CHECK IF BALANCE AFTER WITHDRAWAL IS LESS THAN MINIMUM ALLOWED BALANCE AND ASK USER TO TRY AGAIN
                        if balanceAfterWithdraw < minimumBalance:
                            print (f'Insufficient remaining balance after withdrawal.\n You must have a minimum balance of  {currency} {minimumBalance}. Try Again: \n')
                            continue
                        # CHECK IF WITHDRAWAL AMOUNT IS GREATER THAN MAXIMUM WITHDRAWAL LIMIT AND ASK USER TO TRY AGAIN
                        elif amount > maxWithdrawal:
                            print (f'Sorry. You can not withdraw more than  {currency} {maxWithdrawal} Try Again: \n')
                            continue
                        else:
                            break
                    
                # IF THE USER DOES NOT INPUT WHOLE NUMBERS ASK USER TO TRY AGAIN
                except ValueError:
                    print ('Invalid input. Please enter a number')
                    continue
            
            # HOLD CURRENCY AND AMOUNT SPECIFIED BY USER
            return currency,amount
                
        # RUN THE WITHDRAWAL REQUEST FUNCTION
        while True: 
            # SAVE CURRENCY AND AMOUNT SPECIFIED BY USER INTO THE VARIABLE
            withdrawalValues = withdrawRequest()
            # SAVE CURRENCY SPECIFIED BY USER INTO THE VARIABLE
            currency = withdrawalValues[0]
            # SAVE AMOUNT SPECIFIED BY USER INTO THE VARIABLE
            amount = withdrawalValues[1]
            # PROMPT USER TO CONFIRM WITHDRAWAL AMOUNT
            print ('******************************************* CONFIRM WITHDRAWAL AMOUNT *******************************************\n \n')
            confirmation = input(f'Please confirm withdrawal amount: {currency}  {amount}\n Y to continue / N to change amount: ').upper()
            # IF THE USER INPUT IS INCORRECT ASK FOR CORRECT INPUT
            if confirmation not in ('Y', 'N'):
                print ("        Sorry I didn't understand that. Please start again.")
                continue
            # IF THE USER SAYS NO ALLOW USER CHANGE VALUES
            elif confirmation == 'N':
                continue

            # IF THE USER SAYS YES CONFIRM SUCCESSFUL WITHDRAWAL IN NEXT STEP
            elif confirmation == 'Y':
                break
        
        # DISPLAY SUCCESSFUL WITHDRAWAL MESSAGE
        print ('\n      ------------------------------- SUCCESSFUL WITHDRAWAL   -------------------------------\n')
        # SAVE THE WITHDRAWN AMOUNT AND CURRENCY
        amountWithdrawn = amount
        currencyWithdrawn = currency
        # DISPLAY AMOUNT WITHDRAWN TO USER
        print (f'       Successful Withdrawal of {currencyWithdrawn} {amountWithdrawn}')
        balance = int(session['balance'])
        # DISPLAY USERS PREVIOUS BALANCE
        print (f'       Previous Balance: {currencyWithdrawn} {balance}')
        # SUBTRACT WITHDRAWN AMOUNT FROM USERS CURRENT BALANCE AND SAVE IT TO newBalance VARIABLE
        newBalance = balance - amountWithdrawn
        # UPDATE USERS BALANCE TO WITH NEW BALANCE
        balance = newBalance
        # DISPLAY USERS UPDATED BALANCE
        print (f'New Balance:  {currencyWithdrawn} {balance}')
        print (''' 
        ---------------------------------------------------------------------------------------
        *                      Thank You For Banking With Us.                                  *        
        *                         Gamma International Bank                                     *    
        *                We don't except a big deposit, but small deposits add up.             *     
        ----------------------------------------------------------------------------------------
                ''')

        # HOLD USERS SPECIFIED CURENCY, AMOUNT AND CURRENT BALANCE AFTER WITHDRAWAL
        return currencyWithdrawn, amountWithdrawn, newBalance

    # MOBILE MONEY FUNCTION
    def pesa():
        print('******************************************* MOBILE MONEY WITHDRAWAL*******************************************\n \n')
        print("Select Your Network Provider\n1) SAFARICOM\n2) AIRTEL\n3) TELKOM \n \n")
        while True:
            try:
                userService = str(input("Select option number 1, 2, 3: "))
                if userService == "1":
                    print ('M-PESA MOBILE MONEY WITHDRAWAL')
                    break
                elif userService == "2":
                    print ('AIRTEL-MONEY CASH WITHDRAWAL')
                    break
                elif userService == "3":
                    print ('T-KASH MONEY WITHDRAWAL')
                    break
                else:
                    print("Sorry Incorrect Input. Try Again")
                    continue
            except ValueError:
                print("Sorry Incorrect Input. Try Again")
                continue
        
        while True:
            print("A Transaction Code has been sent to your phone number")
            transactionCode = random.randint(100000,999999)
            print (f"Transaction Code: {transactionCode}")
            try:
                userTransactionCode = int(input("Kindly input the code sent to your number: "))
                if userTransactionCode == transactionCode:
                    while True:
                        print("How much would you want to withdraw?")
                        try:
                            pesaAmount = int(input("Enter amount: "))
                            if pesaAmount <= 2000:
                                print (f"Confirm withdrawal of KSH {pesaAmount}")
                                while True:
                                    pesaConfirm = str(input("Type 'Y' to confirm / 'N' to cancel:  ")).upper()
                                    if pesaConfirm not in ('Y', 'N'):
                                        print ("Invalid input. Try again.")
                                        continue
                                    elif pesaConfirm == 'Y':
                                        while True:
                                            pesaPin = random.randint(1000,9999)
                                            print ("Enter pesa pin to confirm")
                                            print (f"pesa PIN = {pesaPin}")
                                            pesaPinValid = int(getpass.getpass(" Enter pesa Pin: "))
                                            if pesaPinValid == pesaPin:
                                                print("Successful Withdrawal!")
                                                pause = input('Press Enter to return to the main menu. ')
                                                return atmMenu()
                                            elif pesaPinValid != pesaPin:
                                                print('Sorry Pin codes do not match. Please Try again.')
                                                continue
                                    elif pesaConfirm == 'N':
                                        break
                                    else:
                                        print ("Invalid input. Try again.")
                                        continue
                                break
                            elif pesaAmount > 2000:
                                while True:
                                    pesaContinue = str(input("Unsuccessful. You cannot withdraw more than KSH 2000\n \nWould you like to try again or return to the main Menu?\n \n Type 'Y' to try agin or Type 'N' to return to the main Menu:  ")).upper()
                                    # IF THE USER INPUT IS INCORRECT ASK FOR CORRECT INPUT
                                    if pesaContinue not in ('Y', 'N'):
                                        print ('Invalid Input, try again.')
                                        continue
                                    # IF USER SAYS YES RESTART FUNCTION AND TAKE CORRECT AMOUNT INPUT
                                    elif pesaContinue == 'Y':
                                        break
                                    # IF USER SAYS NO RETURN TO THE MAIN MENU
                                    elif pesaContinue == 'N':
                                        return atmMenu()
                                continue
                        except ValueError:
                            print ('Invalid input. Please enter a number')
                            continue
                    break 
                else:
                    print("Sorry Incorrect Code. Try Again")
                    continue
            except ValueError:
                print("Sorry Incorrect Code. Enter the 6 digit code")
                continue

    # PRINT RECEIPT FUNCTION
    def rcptPrint(withdrawn):
        # CHECK IF USER WOULD LIKE TO PRINT A RECEIPT FOR THE TRANSACTION
        while True:
            optn = input("Do you want a receipt for your transaction? (Y/N):  ").upper()
            # CHECK IF THE USER SAYS YES AND PRINT A RECEIPT FOR THE TRANSACTION i.e DISPLAY SPECIFICS OF THE TRANSACTION
            if optn == "Y":
                print('\n     ----------------------------------Transaction Receipt---------------------------------')
                print('     *                                                                                    *')
                print('     *               TRANSACTION IS NOW COMPLETE.                                         *')
                print('     *                                                                                    *')
                print('     *               Transaction number:' +str(random.randint(100000000000,999999999999))+'                                      *')
                print('     *                                                                                    *')
                print('     *               Account Name: '+str(session['username']).upper()+'                                                    *')
                print('     *                                                                                    *')
                print('     *               Amount Withdrawn: '+str(withdrawn[0])+" "+str(withdrawn[1])+'                                          *')
                print('     *                                                                                    *')
                print('     *               Available Balance: '+str(withdrawn[2])+'                                             *')
                print('     *                                                                                    *')
                print('     *               ' + str(now) + '                                           *') 
                print('     *                                                                                    *')
                print('     --------------------------------------------------------------------------------------')
                print('     *                      Thank You For Banking With Us.                                *')
                print('     *                         Gamma International Bank                                   *')
                print("     *                We don't except a big deposit, but small deposits add up.           *")
                print('     --------------------------------------------------------------------------------------')
                break
            # CHECK IF THE USER SAYS NO STOP THE LOOP
            elif optn == "N":
                break   
            # CHECK IF THE USER INPUT IS INCORRECT AND ASK FOR THE CORRECT INPUT
            else:
                print("Wrong command!  Enter 'Y' for Yes and 'N' for No.")
                continue
        return

    # CHECK CURRENT BALANCE FUNCTION
    def crntBalance():    
        while True:
            print ('******************************************* BALANCE CHECK *******************************************\n \n')
            currency = str(input("What account balance would you like to check: \nType 'K' for KSH or 'D' for USD: ")).upper()
            if currency == 'K':
                currency = 'KSH'
                break                    
            elif currency == 'D':
                currency = 'USD'
                break
            else:
                print("Invalid Input. Please Type 'K' for KSH or 'D' for USD")        
                continue

        availableBalance = balance
        print (('Your available {currency}  account balance is:\n \n').upper())
        print (currency +' '+ str(availableBalance ))
         
    # USER LOGIN IDENTITY VERIFICATION FUNCTION
    def userLogin( username):
        for userdata in userArray:
            sessiondata = {' username':"unknown", 'pin':'0000', 'balance':0 }
            # Checks for user existence and says a welcome message
            if  username == userdata['username']:
                found = True
                sessiondata = userdata #Transfers the found users bank info in to sessiondata variable
                break  
            else:
                found = False
                pass    
        return sessiondata          
        # return sessiondata # Returns the value of sessiondata after userLogin() is run,  so we can use in the continuing code 


    def updatePin():
        #user inputs pin
        print("A confirmation code has been sent to your phone \n \n")
        verificationCode = random.randint(1000,9999)
        print(verificationCode)
        #after the user has been verified, he/she proceeds with the change
        while True:
            codeVerify = int(input("Enter verification code here: "))
            if codeVerify == verificationCode:
                while True:
                    newPin = int(getpass.getpass(" Enter new 4 digit pin: "))
                    newPinConfirm = int(getpass.getpass(" Please repeat new 4 digit pin: "))
                    if newPin == newPinConfirm:
                        print("Congratulations! Your pin has been changed!")
                        session['pin'] = newPin
                        pause = input('Press Enter to return to the main menu. ')
                        break
                    elif newPin != newPinConfirm:
                        print('Sorry Pin codes do not match. Please Try again.')
                        continue
                break
            elif codeVerify != verificationCode:
                print("Wrong Verification code entered. Please enter code again")
                continue
        return
        
    # USER LOGIN PIN VERIFICATION FUNCTION
    def pinVerify( pin):
        def pinChangeRequest():
            while True:
                pinChange = str(input('Forgot Pin? Reset (Y/N):  ')).upper()
                if pinChange == 'Y':
                    updatePin()
                    return atmMenu()
                elif pinChange == 'N':
                    print('''            
                                ---------------------------------------------------------------------------------------
                                *                      Thank You For Banking With Us.                                  *        
                                *                         Gamma International Bank                                     *    
                                *                We don't except a big deposit, but small deposits add up.             *     
                                ----------------------------------------------------------------------------------------''')
                    exit()
                else:
                    print ('Invalid input. Try again')
                    continue
        valid = False
        for attempt in range(4):
            print ("\nEnter your pin to Proceed\n")
            pin = str(getpass.getpass("Enter your pin: "))
            if  pin == pin :
                valid = True
                break
            else:
                print ('Incorrect Pin. Try again')
                continue
        if attempt == 3:
            pinChangeRequest()
        return atmMenu() 
    
    # STORE USER'S  username INPUT TO SPECIFIED VARIABLE
    username = str(input("Enter your username: ")).lower()
    # RETRIEVE SPECIFIED USER DETAILS FROM DICTIONARY TO SPECIFIED VARIABLE
    session = userLogin(username)
    # RETRIEVE SPECIFIED USER PIN AND STORE TO VARIABLE
    pin = str(session['pin'])
    # RETRIEVE SPECIFIED USER BALANCE AND STORE TO VARIABLE
    balance = session['balance']
    # RUN PIN VERIFICATION FUNCTION
    pinVerify( pin)

    exit()

# OPTION SELECTOR
print ("\n \n******************************************* WELCOME TO GAMMA INTERNATIONAL BANK ATM *******************************************\n \n")
while True:
    try:
        print ("Select a choice to continue\n \n")
        opt = int(input('1) REGISTER  2)TRANSACT  3) QUIT\n \n'))
        if opt == 1:
            create_user()
        elif opt == 2:
            transact()
        elif opt == 3:
            print('''                                    
                        ---------------------------------------------------------------------------------------
                        *                      Thank You For Banking With Us.                                  *        
                        *                         Gamma International Bank                                     *    
                        *                We don't except a big deposit, but small deposits add up.             *     
                        ----------------------------------------------------------------------------------------''')
            exit()
            
        else:
            print ('Invalid input. Type 1 or 2 to make a selection')
            continue
    except ValueError:
        print ('Invalid input. Type 1 or 2 to make a selection')
        continue

