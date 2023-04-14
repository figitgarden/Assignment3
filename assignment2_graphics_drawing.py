from turtle import *
import random

#parent class
class Drawing:
    def __init__(self, x, y, size, color):
       self.x = x
       self.y = y
       self.size = size
       self.color = color

    def draw(self, x, y):
        goto(x, y)
        for i in range():
            
          forward()
          left()

#child class1 / object1
class Triangles1(Drawing):
    def __init__ (self, x, y, size, color):
        super().__init__(x, y, size, color)
    #draw single triangle
    def draw_triangle(self): 
        penup() 
        goto(self.x, self.y) 
        pendown() 
        for i in range(3): 
            forward(self.size) 
            left(120)
            color('green')
#draw group of 7
for i in range(7):    
    randomone = random.randint(-200, 200) 
    randomtwo = random.randint(-200, 200) 
    tr1 = Triangles1(randomone, randomtwo, 100, color) 
    tr1.draw_triangle() 


#child class2 /object2
speed(20)
class Triangles2(Drawing):
    def __init__ (self, x, y, size, color):
        super().__init__(x, y, size, color)
    
    def draw_triangle(self): 
        penup() 
        goto(self.x, self.y) 
        pendown() 
        for i in range(3): 
            forward(self.size) 
            left(120)
            color('light pink')
#draw a group of 27
for i in range(27):    
    randomone = random.randint(-500, 500) 
    randomtwo = random.randint(-500, 500) 
    tr2 = Triangles2(randomone, randomtwo, 200, color) 
    tr2.draw_triangle()

#child class3 / object3
speed(5)
class Triangles3(Drawing):
    def __init__ (self, x, y, size, color):
        super().__init__(x, y, size, color)

    def draw_triangle(self): 
    # penup() 
        goto(self.x, self.y) 
        # pendown() 
        for i in range(3): 
            backward(self.size) 
            left(120)
            color('navy')
#draw a group of 5
for i in range(5):
    randomone = random.randint(-300, 300) 
    randomtwo = random.randint(-300, 300) 
    tr3 = Triangles3(randomone, randomtwo, 700, "navy") 
    tr3.draw_triangle()
    


exitonclick()