# make python program for cafe menu

#we will use dictionary & conditional statement for this program

#first make set dictionary 

#CafeManagement Program
menu = {
    "Pizza" : 50,
    "Sandwitch" : 80,
    "Pasta" : 65,
    "Thandai" : 20
}



print('welcome to our Swad Restaurant')

print("Pizza: Rs.50\nSandwitch : Rs.80\nPasta: Rs.65\nThandai: Rs.20 ")

order_total = 0    #---work like a diary - jo bhi value dalenge wo store ho jaayegi

#ab user apna pehla order create karega wo item-1 me save hoga.
#so Create item-1
item_1 = input("Enter the name of item you order = ")

#ab jo item user ne dala hai wo hamare store me hai ya nahi isliye CONDITION STATEMENT apply hoga

if item_1 in menu:
    order_total += menu[item_1] #0+50
    print(f"Your Item {item_1} has been added to your order")

else:
    print(f"Please Order something that we can serve")  


#we will make 2nd variable as ANOTHER ORDER--
item_2 = input("Anything else you want = ")

if item_2 in menu:
    order_total += menu[item_2] #0+50
    print(f"Your another order is {item_2}added for the order")
else:
    print(f"your {item_2} is not available")

print(f"The total bill of your order is {order_total} INR.")


