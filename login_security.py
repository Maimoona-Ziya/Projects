#Login Security with multiple conditions

#taking inputs from user

failed_attempts = 0

for i in range(1,4):
    username = input("Enter username : ")                   #Inside loop input taking should be naa..
    password = input("Enter password : ")
    
    if username.lower() == "maimoonaziya" and password == "maimoona@123" :
        acc_status = input("Account status (y/n) : ")
        
        if acc_status.lower().strip() == "y" :

            otp = int(input("Enter OTP : "))

            if otp == 1234 :
                print("Logged in successfully..")
                break
            
            else :
                print("Incorrect OTP")
                failed_attempts += 1 

        else :
            print("Account is inactive.") 
            failed_attempts += 1

    else :                                                   #Else here otherwise indentation error
        print("Incorrect username or password")
        failed_attempts += 1

if failed_attempts >= 3 : 
     print("ACCOUNT LOCKED : ACCOUNT IS LOCKED DUE TO 3 FAILED LOGIN ATTEMPTS..")

    
    
    

    
    