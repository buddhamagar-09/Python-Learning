# Create a mobile phone dial pad using 2d collection

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for collection in num_pad:
    for number in collection:
        print(number, end=" ")
    print()