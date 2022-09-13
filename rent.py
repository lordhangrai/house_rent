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

# ROOMS INFO
def Rooms_Info():
 print("   ------ HOTEL ROOMS INFO ------")
 print("")
 print("STANDARD NON-AC")
 print("---------------------------------------------------------------")
 print("Room amenities include: 1 Double Bed, Television, Telephone,")
 print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
 print("an attached washroom with hot/cold water.\n")
 print("STANDARD NON-AC")
 print("---------------------------------------------------------------")
 print("Room amenities include: 1 Double Bed, Television, Telephone,")
 print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
 print("an attached washroom with hot/cold water + Window/Split AC.\n")
 print("3-Bed NON-AC")
 print("---------------------------------------------------------------")
 print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
 print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
 print("Side table, Balcony with an Accent table with 2 Chair and an")
 print("attached washroom with hot/cold water.\n")
 print("3-Bed AC")
 print("---------------------------------------------------------------")
 print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
 print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
 print("1 Side table, Balcony with an Accent table with 2 Chair and an")
 print("attached washroom with hot/cold water + Window/Split AC.\n\n")
 print()
 n=int(input("0-BACK\n ->"))
 if n==0:
  Home()
 else:
  exit()

 ph=int(input("Customer Id: "))
 global i
 f=0
 r=0
 for n in range(0,i):
  if custid[n]==ph and p[n]==0:
   f=1
   print("-------------------------------------------------------------------------")
   print("       Hotel AnCasa")
   print("-------------------------------------------------------------------------")
   print("       Menu Card")
   print("-------------------------------------------------------------------------")
   print("\n BEVARAGES        26 Dal Fry................ 140.00")
   print("----------------------------------  27 Dal Makhani............ 150.00")
   print(" 1 Regular Tea............. 20.00  28 Dal Tadka.............. 150.00")
   print(" 2 Masala Tea.............. 25.00")
   print(" 3 Coffee.................. 25.00  ROTI")
   print(" 4 Cold Drink.............. 25.00  ----------------------------------")
   print(" 5 Bread Butter............ 30.00  29 Plain Roti.............. 15.00")
   print(" 6 Bread Jam............... 30.00  30 Butter Roti............. 15.00")
   print(" 7 Veg. Sandwich........... 50.00  31 Tandoori Roti........... 20.00")
   print(" 8 Veg. Toast Sandwich..... 50.00  32 Butter Naan............. 20.00")
   print(" 9 Cheese Toast Sandwich... 70.00")
   print(" 10 Grilled Sandwich........ 70.00  RICE")
   print("          ----------------------------------")
   print(" SOUPS         33 Plain Rice.............. 90.00")
   print("----------------------------------  34 Jeera Rice.............. 90.00")
   print(" 11 Tomato Soup............ 110.00  35 Veg Pulao.............. 110.00")
   print(" 12 Hot & Sour............. 110.00  36 Peas Pulao............. 110.00")
   print(" 13 Veg. Noodle Soup....... 110.00")
   print(" 14 Sweet Corn............. 110.00  SOUTH INDIAN")
   print(" 15 Veg. Munchow........... 110.00  ----------------------------------")
   print("          37 Plain Dosa............. 100.00")
   print(" MAIN COURSE       38 Onion Dosa............. 110.00")
   print("----------------------------------  39 Masala Dosa............ 130.00")
   print(" 16 Shahi Paneer........... 110.00  40 Paneer Dosa............ 130.00")
   print(" 17 Kadai Paneer........... 110.00  41 Rice Idli.............. 130.00")
   print(" 18 Handi Paneer........... 120.00  42 Sambhar Vada........... 140.00")
   print(" 19 Palak Paneer........... 120.00")
   print(" 20 Chilli Paneer.......... 140.00  ICE CREAM")
   print(" 21 Matar Mushroom......... 140.00  ----------------------------------")
   print(" 22 Mix Veg................ 140.00  43 Vanilla................. 60.00")
   print(" 23 Jeera Aloo............. 140.00  44 Strawberry.............. 60.00")
   print(" 24 Malai Kofta............ 140.00  45 Pineapple............... 60.00")
   print(" 25 Aloo Matar............. 140.00  46 Butter Scotch........... 60.00")
   print("Press 0 -to end ")
   ch=1
   while(ch!=0):
    
    ch=int(input(" -> "))
    
    # if-elif-conditions to assign item
    # prices listed in menu card
    if ch==1 or ch==31 or ch==32:
     rs=20
     r=r+rs
    elif ch<=4 and ch>=2:
     rs=25
     r=r+rs
    elif ch<=6 and ch>=5:
     rs=30
     r=r+rs
    elif ch<=8 and ch>=7:
     rs=50
     r=r+rs
    elif ch<=10 and ch>=9:
     rs=70
     r=r+rs
    elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
     rs=110
     r=r+rs
    elif ch<=19 and ch>=18:
     rs=120
     r=r+rs
    elif (ch<=26 and ch>=20) or ch==42:
     rs=140
     r=r+rs
    elif ch<=28 and ch>=27:
     rs=150
     r=r+rs
    elif ch<=30 and ch>=29:
     rs=15
     r=r+rs
    elif ch==33 or ch==34:
     rs=90
     r=r+rs
    elif ch==37:
     rs=100
     r=r+rs
    elif ch<=41 and ch>=39:
     rs=130
     r=r+rs
    elif ch<=46 and ch>=43:
     rs=60
     r=r+rs
    elif ch==0:
     pass
    else:
     print("Wrong Choice..!!")
   print("Total Bill: ",r)
   
   # updates restaurant charges and then
   # appends in 'rc' list
   r=r+rc.pop(n)
   rc.append(r) 
  else:
   pass
 if f == 0:
  print("Invalid Customer Id")
 n=int(input("0-BACK\n ->"))
 if n==0:
  Home()
 else:
  exit()
    
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
    print("\n Amount: ",(price[n]*day[n])+rc[n])
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
