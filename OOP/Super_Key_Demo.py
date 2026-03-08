
class shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Rectagnle(shapes):
    def __init__(self,name,color,is_filled,length,breadth):
        super().__init__(color,is_filled)
        self.name = name
        self.length = length
        self.breadth = breadth
    def display_details(self):
        print(f" Shape: {self.name} \n Length: {self.length} \n Breadth: {self.breadth}")
        print(f"The {self.name} of length {self.length} and breadth {self.breadth} is {'filled' if self.is_filled else 'not filled'} with {self.color} color.")


class Square(shapes):
    def __init__(self,name,color,is_filled,length):
        super().__init__(color,is_filled)
        self.name = name
        self.length = length
    def display_details(self):
        print(f" Shape: {self.name} \n Length: {self.length}")
        print(f"The {self.name} of length {self.length}  is {'filled' if self.is_filled else 'not filled'} with {self.color} color.")

rect = Rectagnle("Rectangle","Red",True,12,23)
sq = Square("Square","Green",False,12)

rect.display_details()
print()
sq.display_details()