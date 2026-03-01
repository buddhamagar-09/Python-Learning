# arbitary functions 
# *args allows you to pass multiple non-key arguments
# **kwargs allows you to pass multiple keyword arguments
#  * unpacking operator

# def sum(*nums):
#     total = 0
#     for num in nums:
#         total += num
    # print(type(nums))
#     return total

# print(sum(1,2,3,4,5))



# using **kwargs

def user_details(**details):
    for key,value in details.items():
       print(f"{key:10} : {value}")
    print()
    print(type(details))

user_details(name="Buddha Saru Magar",
             district="Nawalpur",
             city = "Gaindakot-1",
             Tole = "Prativa Tole"
             )