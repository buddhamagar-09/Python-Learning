

def shipping_address(*args,**kwargs):
    for arg in args:
        print(f"{arg}",end=" ")
    print()

    if "house_no" in kwargs:
        print(f"{kwargs.get('district')} , {kwargs.get('house_no')}")
        print(f"{kwargs.get('city')}")  
        print(f"{kwargs.get('tole')}") 
    else:
        print(f"{kwargs.get('district')}")  
        print(f"{kwargs.get('city')}")  
        print(f"{kwargs.get('tole')}")  


shipping_address("Mr.","Buddha Saru Magar",
                 district = "Nawalpur",
                 city = "Giandakot-1",
                 tole = "Prativa Tole",
                 house_no = 123 )