import turtle

# abstract class
class Shape:
    # constructor
    def __init__(self, sides, length, color):
        self.sides = sides
        self.length = length
        self.color = color
        self.t = turtle.Turtle()
    # abstract method
    def draw(self):
        self.t.pencolor(self.color)
        for _ in range(self.sides):
            self.t.forward(self.length)
            self.t.right(360 / self.sides)

#sub class
class Diamond(Shape):
    def __init__(self, length, color):
        super().__init__(4, length, color)

    def draw(self):
        self.t.pencolor(self.color)
        self.t.right(120)
        self.t.forward(self.length)
        self.t.right(120)
        self.t.forward(self.length)
        self.t.right(60)
        self.t.forward(self.length)
        self.t.right(120)
        self.t.forward(self.length)

           
        


#three instance
#Concrete class
class Square(Shape):
    def __init__(self, length, color):
        print("creating square")
        super().__init__(4, length, color)

class Triangle(Shape):
    def __init__(self, length, color):
        print("creating triangle")
        super().__init__(3, length, color)

class Pentagon(Shape):
    def __init__(self, length, color):
        super().__init__(5, length, color)

# class Diamond(Shape):
#     def __init__(self, length, color):
#         super().__init__(4,length, color)
        



def main():
    turtle.speed(0)
    turtle.bgcolor("navy")

    # square = Square(100, "red")
    # square.draw()

    # triangle = Triangle(100, "blue")
    # triangle.t.penup()
    # triangle.t.goto(-150, 0)
    # triangle.t.pendown()
    # triangle.draw()

    # pentagon = Pentagon(100, "green")
    # pentagon.t.penup()
    # pentagon.t.goto(150, 0)
    # pentagon.t.pendown()
    # pentagon.draw()

    diamond = Diamond(100, "white")
    diamond.t.penup()
    diamond.t.goto(-300, 0)
    diamond.t.pendown()
    diamond.draw()



    turtle.done()

if __name__ == "__main__":
    main()