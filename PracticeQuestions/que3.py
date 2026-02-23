# Temperature Converter 

unit = input("Enter the unit of the temperature C/F : ")
temp = float(input("Enter the Temperature: "))

if unit == "c":
    converted = round(((temp * 9)/5) + 32 , 1)
    print(f"The temperature in Fahrenheit is {converted} F.")

elif unit == "f":
    converted = round((temp-32) * 5/9 , 1)
    print(f"The temperature in Celsius is {converted} C.")
else:
    print("Invalid unit Entered.")


# validate the user Name
# 1 username shouldnt be more than 12 characters
# 2 user name must not contain digits
# 3username mustnt contains white spaces

username = input("Enter your UserName: ")

length = len(username)

if length > 12 :
    print("Username cant be more than 12 characters.")
elif username.find(" ") != -1:
    print("Username cant have white spaces.")
elif not username.isalpha():
    print("Username cant have Numbers or digits.")
else:
    print(f" welcome Back {username}")
