print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

my_share = round(bill*(1 +tip/100)/people, 2)

print(f"Your share is: ${my_share:.2f}") #:.2f makes the print statement print 2 places after the coma every time

# print(type(my_share))