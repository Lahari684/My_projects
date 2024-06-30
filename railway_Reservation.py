
''' for reservation we should know the terms
1.train PNR
2.user details-name,age,gender,phone number
3.login
4.source-destination
5.date&time
6.price
7.seat availability
'''
import random
s='''
1.User details
2.source and destination
3.Train  name & number and seats availability
4.Price
5.Booking Ticket'''
Trains={("Vetapalem","Nellore"):["krishnaexp","bitraguntaexp","pooriexp"],("Ongole","Tirupati"):["janmabhoomiexp","janasathabdhiexp","tirumalaexp"],("Hyderabad","Banglore"):["secundrabadexp","Agartalaexp","vishakaexp"]}
users={"Lahari":1000,"Ramakrishna":2000,
"Chakradhar":3000,"Nagasudha":4000}
trains_available={"krishnaexp":[22894,200,250],"bitraguntaexp":[234567,100,150],"pooriexp":[905567,150,200],"Secundrabadexp":[345664,210,300],"vishakaexp":[234567,80,540],"janmabhoomiexp":[210002,24,194],"janasathabdhiexp":[888802,283,390],"tirumala":[77777,300,2040]}
user_details=[]
user=input("Please enter the User Name:")
if user in users.keys():
    password=int(input("Please Enter the password:"))
    print("Thankyou for visiting the website of South Central Railway Of India")
    if password==users[user]:
       print(s)
       print("SELECT YOUR REQUIRED OPTION:")
else:
    print("No user found.Please register in order to reserve")
option=int(input())
if option ==1:
    name=input("please Enter your name:")
    password_new=int(input("Enter the new password:"))
    mobile_num=int(input("Enter your mobile number:"))
    age=int(input("Enter your age:"))
    gender=input("Enter your gender:")
    details=[mobile_num,age,gender,name,password]
    user_details.append(details)
elif option==2:
    source=input("enter your source:")
    destination=input("Enter your destination:")
    for i in Trains:
        if source in ("Vetapalem","Nellore"):
            if destination in ("Vetapalem","Nellore"):
               print(Trains[("Vetapalem","Nellore")])
               break
        elif source in ("Ongole","Tirupati"):
            if destination in ("Ongole","Tirupati"):
               print(Trains[("Ongole","Tirupati")])
               break
        elif source in ("Hyderabad","Banglore"):
            if destination in ("Hyderabad","Banglore"):
               print(Trains[("Hyderabad","Banglore")])
               break
        else:
            print("No Trains are available")
            break
elif option==3:
    Train_Name=input("Please enter the train name:")
    if Train_Name in trains_available:
        print(Train_Name)
        print("Train Number is:",trains_available[Train_Name][0])
        print("seat_availability:",trains_available[Train_Name][1])
elif option==4:
    Train_Name=input("Please enter the Train name:")
    price=trains_available[Train_Name][2]
    print("The ticket price is:",price)
elif option==5:
    user_name=input("please enter the name:")
    age=int(input("Please Enter your age:"))
    t=input("Enter the train name:")
    Trains={"krishnaexp":["Vijayawada","Nellore"],"bitraguntaexp":["Vijayawada","Nellore"],"pooriexp":["Vizag","Goa"],"janmabhoomiexp":["Ongole","Tirupati"],"janasathabdhiexp":["Pune","Tirupati"],"tirumalaexp":["Ongole","Gujarat"],"secundrabadexp":["Hyderabad","Banglore"],"Agartalaexp":["vellore","Banglore"],"vishakaexp":["Hyderabad","pune"]}
    if t in trains_available:
       print("****************South Central Railway of India******************")
       print("Name of the passenger:",user_name)
       print("Age:",age)
       print("You are travelling between:",Trains.get(t))
       print("Train Number is:",trains_available[t][0])
       print("your seat_number is:",random.randint(0,trains_available[t][1]))
       print("Total price of your ticket is:",trains_available[t][2],"RS/-only")
       print("**********************Thankyou for booking**********************")
    else:
        print("No Such Train Exists")
