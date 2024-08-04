print("Welcome to tip calculator")
x=float(input("what was the total bill: $"))
y=int(input("how much tip would you like to  give 10,12 0r 15:$"))
yy=y/100
z=int(input("how many people to split the bill "))
total=(x+(x*yy))/z
print(f"each person should pay: $ {total:.2f}")





