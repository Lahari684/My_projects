print("*"*34)
accountholders_names=['a','b','c','d']
accountholders_pinnumbers=['1111','2222','3333','4444']
accountholders_balances=[100000,233445,984603,100000]
deposit_amount=0
withdraw_amount=0
balance=0
counter_1=1
counter_2=5
i=0
while True:
    print("-"*3,"WELCOME TO THE INDIAN BANK","-"*3)
    print("*"*34)
    print("1. open a new account")
    print("2. Withdraw the amount")
    print("3. Deposit the amount")
    print("4. check the Balance and enquiry")
    print("5. exit")
    print("*"*34)
    option=int(input("Enter your selected number:"))
    if option==1:
        print("You had selected the option to open a new account")
        name=input("Enter the Name:")
        accountholders_names.append(name)
        pin=str(input("Please set the pin:"))
        accountholders_pinnumbers.append(pin)
        balance=0
        deposit_amount=int(input("Enter the amount you want to deposit:"))
        balance=balance+deposit_amount
        accountholders_balances.append(balance)
        print("\nname:",end=" ")
        print(accountholders_names[-1])
        print("pin:",end=" ")
        print(accountholders_pinnumbers[-1])
        print("balance:",end=" ")
        print(accountholders_balances[-1],end="")
        print("-/Rs")
        print("Sucessfully an account has created in this bank")
        print("Please remember your pin number and account name")
        mainmenu=input("please press enter to go to main menu")
    elif option==2:
        j = 0
        print("you had selected the option to withdraw your amount")
        k = -1
        name = input("Please input name : ")
        pin = input("Please input pin : ")
        while k < len(accountholders_names) - 1:
            k = k + 1
            if name == accountholders_names[k]:
                if pin == accountholders_pinnumbers[k]:
                    j = j + 1
                    print("Your Current Balance:", end=" ")
                    print(accountholders_balances[k], end=" ")
                    print("-/Rs\n")
                    balance=accountholders_balances[k]
                    withdrawal = int(input("amount to Withdraw : "))
                    if balance > withdrawal:
                        print("you have with drawn an Amount of:",withdrawal)
                        balance=balance-withdrawal
                        print("The balance available in your account now is:",balance)
                    if withdrawal > balance:
                           print("Insufficient balance please deposit some amount to withdraw")
                           deposit_amount = int(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                           balance = balance + deposit_amount
                           print("Your Current Balance:", end=" ")
                           print(balance, end=" ")
                           print("-/Rs\n")
                           balance = balance - withdrawal
                           print("-\n")
                           print("----Withdraw Successfull!----")
                           accountholders_balances[k] = balance
                           print("Your New Balance: ", balance, end=" ")
                           print("-/Rs\n\n")
                if j < 1:
                   print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif option==3:
        m = 0
        print("you had selected the option to withdraw your amount")
        k = -1
        name = input("Please input name : ")
        pin = input("Please input pin : ")
        while k < len(accountholders_names) - 1:
            k = k + 1
            if name == accountholders_names[k]:
                if pin == accountholders_pinnumbers[k]:
                    m = m + 1
                    print("Your Current Balance:", end=" ")
                    print(accountholders_balances[k], end=" ")
                    print("-/Rs\n")
                    balance=accountholders_balances[k]
                    deposit_amount= int(input("enter the amount you want to deposit: "))
                    deposit_amount=deposit_amount+accountholders_balances[k]
                    print("The balance available in your account after depositing is:",deposit_amount,"-\n")
                if m < 1:
                   print("Your name and pin does not match!\n")
                break
        mainmenu=input("please press enter to exit and go back into main menu")
    elif option==4:
        print("You had selected the option to check balance and enquiry")
        k=0
        print("account holder names and their balances mentioned below")
        print("\n")
        while k<=len(accountholders_names)-1:
            print("accountholder names:",accountholders_names[k])
            print("accountholder balances:",accountholders_balances[k],"-/Rs")
            k=k+1
        mainmenu=input("please press enter to exit and go back into main menu")
    elif option==5:
        print("Thank you for visting indian bank")
        print("Please visit again")
        print("Have a good day")
        break
    else:
        print("Invalid option entered")
        print("Please Try Again!")
        mainmenu=input('Please press enter to get back to the main menu ')


