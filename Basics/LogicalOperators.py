# Logical Operators and, or, not
# and - both conditions must be true
# or - at least one condition must be true
# not - negates the condition
# Example of and
a = 5
b = 10
if a > 0 and b > 0:
    print("Both a and b are positive numbers.")

# Example of or
if a > 0 or b < 0:
    print("At least one of a or b is a positive number.")

# Example of not
if not a < 0:
    print("a is not a negative number.")



# ternary Operators using if else statement in one line 
# Formula or syantax 
# X if condition else Y

num = 5
result = "Even" if num % 2 == 0 else "Odd"
print("The number is " + result)