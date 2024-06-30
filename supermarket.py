from datetime import datetime
name=input("Enter your name:")
lists='''
rice    rs 80/kg
wheat   rs 50/kg
corn    rs 24/kg
oil     rs 150/kg
panner  rs 110/kg
boost   rs 900/kg
colgate rs 67/kg
flour   rs 30/kg'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]
#rates for items
items={'rice':80,'wheat':50,'corn':24,'oil':150,'panner':110,'boost':900,'colgate':67,'flour':30}
option=int(input("for items in list press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit :"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter your required quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*6)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered items are not available ")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"-","Lahari Supermarket",25*"-")
            print(25*"-","Vetapalem",25*"-")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(76*"-")
            print("sno",5*" ","items",5*" ",'Quantity',5*" ",'price')
            for i in range(len(pricelist)):
                 print(i+1,4*" ",2*" ",ilist[i],5*" ",qlist[i],12*" ",plist[i])
                 print(75*" ")
                 print(50*" ",'Total amount:','Rs',totalprice)
                 print(50*" ","gst amount",'Rs',gst)
                 print(75*" ")
                 print(50*" ",'final amount:','Rs',finalamount)
                 print(75*" ")
                 print(25*" ",'Thanks for visting')
                 print(75*"-")
                    