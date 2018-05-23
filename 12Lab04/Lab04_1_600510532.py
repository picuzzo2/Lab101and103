class Circle:
    #Constructor
    def __init__(self,radius=None):
        self.radius = radius

    #Perimeter
    def perimeter(self):
        return 2*(3.14)*(self.radius)

    #Area
    def area(self):
        return (3.14)*(self.radius)*self.radius

class Rectangle:
    #Constructor
    def __init__(self,w,h):
        self.w = w
        self.h = h

    #Perimeter
    def perimeter(self):
        return 2*self.h + 2*self.w

    #Area
    def area(self):
        return self.w*self.h


def main():
    c = Circle(8)
    r = Rectangle(10,12)
    print(c.perimeter())
    print(c.area())
    print(r.perimeter())
    print(r.area())

if __name__ == '__main__':
    main()