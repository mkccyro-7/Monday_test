bis = int(input("enter number of biscuits "))

if bis == 3:
    print("Not eaten")
elif 0 < bis < 3:
    print("partly eaten")
elif bis == 0:
    print("fully eaten")
else:
    print("Enter 3 or any other number less than 3")
