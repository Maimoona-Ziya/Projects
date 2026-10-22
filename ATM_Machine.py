#ATM MACHINE MINI PROJECT using Python basic concepts.(without using for/while loop) 
#Services provided by this ATM Machine are:
#1. CASH WITHDRAWAL
#2. BALANCE ENQUIRY
#3. CASH DEPOSIT
#4. EXIT

#Greeting the user.
print("*"*70)
print("                   WELCOME TO OUR ATM MACHINE !")
print("*"*70)

#Asking user to insert their card.
print("Please insert your Credit/Debit Card")
print("-"*25 +"PROCESSING"+ "-"*29)


#Taking PIN as input from user
pin = input("Enter your 4 digit PIN : ")              #taking input as str to include 0 as leading digit in PIN
balance = 100000.00
pin = pin.strip()                                     #To remove any leading or trailing spaces

#Checking if the PIN is 4 digits or not.
if len(pin) == 4 :       
    #Checking if the PIN entered is numeric or not. 
    numbers = "0123456789"
    if pin[0] in numbers and pin[1] in numbers and pin[2] in numbers and pin[3] in numbers:

        #Asking user to select the service as per their need.                                                    
        print("Select the required service :")
        print("1. CASH WITHDRAWAL")
        print("2. BALANCE ENQUIRY")
        print("3. CASH DEPOSIT")
        print("4. EXIT")
        choice = int(input("Enter your choice : "))


        #CASH WITHDARAWAL 
        if choice == 1 :
            withdraw_amount = int(input("Enter the amount to withdraw : ₹"))
            
            #Checking if the withdraw amount entered by the user can be withdrawn or not.
            if withdraw_amount % 100 == 0 and withdraw_amount >= 500 and withdraw_amount <= balance : 
                print("-"*25 +"WITHDRAWN SUCCESSFULLY"+ "-"*25)
                balance = balance - withdraw_amount
                print("Please collect your cash and card.")
                         
                #Asking user if they want a receipt or not.
                receipt_print = input("Do you want a receipt? (Y/N) : ")
            
                if receipt_print.upper().strip() == "Y" :
                    print("-"*25 +"RECEIPT"+ "-"*25)
                    print("Amount Withdrawn : ₹", withdraw_amount)
                    print("Remaining balance : ₹",balance)
                    print("-"*25 +"THANK YOU !"+ "-"*25)
            
                elif receipt_print.upper().strip() == "N" :             #To avoid case sensivity and leading/trailing spaces in user input 
                    print("-"*25 +"THANK YOU !"+ "-"*25)
                                
                else :
                    print("Invalid input. Please try again.")
                    
            elif withdraw_amount > balance :                             #Gemini helped me in including this
                print("Insufficient balance. Please try again.")
                    
            else: 
                print("Minimum amount to withdraw is ₹500 and it should be in multiples of 100.")
    
    
        #BALANCE ENQUIRY
        elif choice == 2 :
            print("-"*25 +"BALANCE ENQUIRY"+ "-"*25) 
            print("Your current balance is : ₹", balance)

            #Asking user if they want a receipt or not.
            receipt_print = input("Do you want a receipt? (Y/N) : ")
        
            if receipt_print.upper().strip() == "Y" :
                print("-"*25 +"RECEIPT"+ "-"*29)
                print("Current Balance : ₹",balance)
                print("-"*25 +"THANK YOU !"+ "-"*25)

            elif receipt_print.upper().strip() == "N" : 
                print("-"*25 +"THANK YOU !"+ "-"*25)

            else :
                print("Invalid input. Please try again.")


        #CASH DEPOSIT
        elif choice == 3 :
            deposit_amount = int(input("Enter the amount to deposit : ₹"))
            print("Please insert cash.")
            print("-"*25 +"CASH DEPOSITED SUCCESSFULLY"+ "-"*25)
            balance = balance + deposit_amount
            print("-"*25 +"THANK YOU !"+ "-"*40)

            #Asking user if they want a receipt or not.
            receipt_print = input("Do you want a receipt? (Y/N) : ")
                
            if receipt_print.upper().strip() == "Y" :
                print("-"*25 +"RECEIPT"+ "-"*29)
                print("Current Balance : ₹",balance)
                print("-"*25 +"THANK YOU !"+ "-"*25)
            
            elif receipt_print.upper().strip() == "N" : 
                print("-"*25 +"THANK YOU !"+ "-"*25)
            
            else :
                print("Invalid input. Please try again.")

 
        #EXIT
        elif choice == 4 :
            print("-"*25 +"THANK YOU !"+ "-"*25)

        #Incase user enters any invalid choice. 
        else :
            print("Invalid choice. Please try again.")
            print("-"*25 +"THANK YOU !"+ "-"*25)

    else :
        print("Invalid PIN. Only numeric values are allowed.")

else :
    print("Invalid PIN. Please try again.")
    print("-"*25 +"THANK YOU !"+ "-"*25)

    