# How do you check if two rectangles overlap with each other? 

class Rectangle():

    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def rectangle_overlap(rect1,rect2):
    if rect1.x1 >= rect2.x2 or rect2.x1 >=rect1.x2:
        return False

    
    if rect1.y1 >= rect2.y2 or rect2.y1 >= rect2.y1:
        return False

    return True


rect1 = Rectangle(0, 0, 2, 2)
rect2 = Rectangle(2, 5, 2, 0)

overlap = rectangle_overlap(rect1,rect2)

if overlap:
    print("Rectangle is Overlap")

else:
    print("Rectangle is do not overlap")

























