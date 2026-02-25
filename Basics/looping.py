import time
# while loop 
# calculate interest

# principal = 0
# rate = 0
# time = 0

# while True:
#     principal = int(input("Enter the Principal amount: "))
#     if principal < 0:
#         print("Principal amount cannot be less than zero.")
#     else:
#         break

# while True:
#     rate = float(input("Enter the rate of the interest: "))
#     if rate < 0:
#         print("Rate cannot be negative.")
#     else:
#         break

# while True:
#     time = float(input("Enter the time of the Interest: "))
#     if time < 0:
#         print("Time cannot be negative.")
#     else:
#         break

# interest = (principal * time * rate)/100
# print(f"The interest after {time} years is Rs.{interest:.2f}")



# for loop for fixed number of time    


# eg iterate for numbers

# for x in reversed(range(1,10)):
#     if x == 6:
#         continue
#     else:
#         print(x)

# iterate in strings
# name = input("Enter your Nmae: ")
# for x in name:
#     print(x)


    # nested looping loop inside another loop
rows = int(input("Enter the Rows: "))
columns = int(input("Enter the Columns: "))
symbol = input("Enter the Symbol you want ($,#,@,^,*,&,!): ")

for x in range(rows):
    for y in range(columns):
        print(symbol,end=" ")
    print()



# create a triangle pattern
# rows = int(input("Enter the number of rows: "))
for x in range(1,6):
    for y in range(x):
        print("*",end=" ")
    print()