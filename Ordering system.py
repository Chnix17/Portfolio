print("""*************PHINMA SOUTH CANTEEN**************
JUNKFOODS:           DRINKS:         
BURGER - 30₱         COKE/ROYAL/SPRITE - 20₱
FRIES - 15₱          WATER - 25₱""")
customer_name = input("Please Enter your name: ")
print("----Good day"
,customer_name,"! "+"Welcome to PHINMA SOUTH CANTEEN!---- ")
item1 = input("Please choose desire food do you want: ")
food1 = int(input("Enter the food price: "))
qty1 = int(input("Enter Qty of the food: "))   
print("******Here is your order: ********")
total1 = food1*qty1
print(qty1,"x",item1,"-",total1,"₱") 
print("your total amount is:",(total1),"₱")                      
cash = int(input("Enter Cash to pay: "))
print("ORDER BY: ",customer_name) 
print("Item: ")
print(qty1,"x",item1,"-",total1,"₱")
print("Total: ",total1)  #Total of purchase
print("Cash amount: ",cash) 
print("Change: ",(cash-total1))
print("   THANK YOU FOR PURCHASING!")
