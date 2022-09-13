import random
import datetime

# Global List Declaration
name = []
phno = []
add = []
price = []
p = []
House_Info = []
Land_Info = []
custid = []
day = []

# Global Variable Declaration

i = 0

# Home Function
def Home():
 
 print("\t\t\t\t\t\t WELCOME TO LORD HOUSE AND LAND BOOKING \n")
 print("\t\t\t 1 Booking\n")
 print("\t\t\t 2 House Info\n")
 print("\t\t\t 3 Land Info\n")
 print("\t\t\t 4 Payment\n")
 print("\t\t\t 5 Record payment\n")
 print("\t\t\t 0 Exit\n")

 ch=int(input("->"))
 
 if ch == 1:
  print(" ")
  Booking()
 
 elif ch == 2:
  print(" ")
  House_Info()
 
 elif ch == 3:
  print(" ")
  Land_Info()
 
 elif ch == 4:
  print(" ")
  Payment()
 
 elif ch == 5:
  print(" ")
  Record()
 
 else:
  exit()

# Function used in booking

def date(c):
 
 if c[2] >= 2019 and c[2] <= 2020:
  
  if c[1] != 0 and c[1] <= 12:
   
   if c[1] == 2 and c[0] != 0 and c[0] <= 31:
    
    if c[2]%4 == 0 and c[0] <= 29:
     pass
    
    elif c[0]<29:
     pass
    
    else:
     print("Invalid date\n")
     name.pop(i)
     phno.pop(i)
     add.pop(i)
     Booking()
   
   
   # if month is odd & less than equal
   # to 7th month
   elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
    pass
   
   # if month is even & less than equal to 7th
   # month and not 2nd month
   elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
    pass
   
   # if month is even & greater than equal
   # to 8th month
   elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
    pass
   
   # if month is odd & greater than equal
   # to 8th month
   elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:
    pass
   
   else:
    print("Invalid date\n")
    name.pop(i)
    phno.pop(i)
    add.pop(i)
    Booking()
    
  else:
   print("Invalid date\n")
   name.pop(i)
   phno.pop(i)
   add.pop(i)
   Booking()
   
 else:
  print("Invalid date\n")
  name.pop(i)
  phno.pop(i)
  add.pop(i)
  Booking()


# Booking function
def Booking():
 
  # used global keyword to
  # use global variable 'i'
  global i
  print(" BOOKING ROOMS")
  print(" ")
  
  while 1:
   n = str(input("Name: "))
   p1 = str(input("Phone No.: "))
   a = str(input("Address: "))
   
   # checks if any field is not empty
   if n!="" and p1!="" and a!="":
    name.append(n)
    add.append(a)
    break
    
   else:
    print("\tName, Phone no. & Address cannot be empty..!!")
   

  # House Information
  print("----SELECT HOUSE TYPE----")
  print(" 1. Royal House ")
  print(" 2. Standard House")
  print(" 3. 8-Bedroom House")
  print(" 4. 6-Bedroom with balcony House")
  print(("\t\tPress 0 for House Prices"))
  
  ch=int(input("->"))
  
  # if-conditions to display 
  # type and it's price
  if ch==0:
   print(" 1. Royal House - Rs. 550000000")
   print(" 2. Standard House - Rs. 40000000")
   print(" 3. 8-Bedroom House - Rs. 45000000")
   print(" 4. 6-Bedroom House - Rs. 5000000")
   ch=int(input("->"))
  if ch==1:
   House_Info.append('Royal House')
   print("House Type- Royal House")
   price.append(550000000)
   print("Price- 550000000")
  elif ch==2:
   House_Info.append('Standard House')
   print("House Type- Standard House")
   price.append(40000000)
   print("Price- 40000000")
  elif ch==3:
   House_Info.append('8-Bedroom House')
   print("House Type- 8-Bedroom House")
   price.append(45000000)
   print("Price- 45000000")
  elif ch==4:
   House_Info.append('6-Bedroom with balcony House')
   print("House Type- 6-Bedroom with balcony House")
   price.append(5000)
   print("Price- 5000")
  else:
   print(" Wrong choice..!!")

# PAYMENT FUNCTION   
def Payment():
 
 ph=str(input("Phone Number: "))
 global i
 f=0
 
 for n in range(0,i):
  if ph==phno[n] :
   
   # checks if payment is
   # not already done
   if p[n]==0:
    f=1
    print(" Payment")
    print(" --------------------------------")
    print(" MODE OF PAYMENT")
    
    print(" 1- Credit/Debit Card")
    print(" 2- Paytm/PhonePe")
    print(" 3- Using UPI")
    print(" 4- Cash")
    x=int(input("-> "))
    print("\n Amount: ",(price[n]))
    print("\n   Pay For AnCasa")
    print(" (y/n)")
    ch=str(input("->"))
    
    if ch=='y' or ch=='Y':
     print("\n\n --------------------------------")
     print("   Hotel AnCasa")
     print(" --------------------------------")
     print("    Bill")
     print(" --------------------------------")
     print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
     print("\n House Type: ",House_Info[n],"\t\n House rent: ",price[n],"\t")
     print(" --------------------------------")
     print("\n Total Amount: ",(price[n]),"\t")
     print(" --------------------------------")
     print("   Thank You")
     print("   Visit Again :)")
     print(" --------------------------------\n")
     p.pop(n)
     p.insert(n,1)
     
     # pops room no. and customer id from list and
     # later assigns zero at same position
     House_Info.pop(n)
     custid.pop(n)
     House_Info.insert(n,0)
     custid.insert(n,0)
     
   else:
    
    for j in range(n+1,i):
     if ph==phno[j] :
      if p[j]==0:
       pass
      
      else:
       f=1
       print("\n\tPayment has been Made :)\n\n")
 if f==0: 
  print("Invalid Customer Id")
  
 n = int(input("0-BACK\n ->"))
 if n == 0:
  Home()
 else:
  exit()

# RECORD FUNCTION
def Record():
 
 # checks if any record exists or not
 if phno!=[]:
  print("  *** House RENTED ***\n")
  print("| Name  | Phone No. | Address  | Check-In | Check-Out  | Room Type  | Price  |")
  print("----------------------------------------------------------------------------------------------------------------------")
  
  for n in range(0,i):
   print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",House_Info[n],"\t|",price[n])
  
  print("----------------------------------------------------------------------------------------------------------------------")
 
 else:
  print("No Records Found")
 n = int(input("0-BACK\n ->"))
 if n == 0:
  Home()
  
 else:
  exit()

# Driver Code
Home()
