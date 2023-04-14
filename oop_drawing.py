from turtle import *
import random
def draw_triangle(x, y, size): 
# penup() 
    goto(x, y) 
    # pendown() 
    for i in range(3): 
        forward(size) 
        left(120)
        color('green')
for i in range(7):
        
    # draw a triangle at a random location 
    randomone = random.randint(-200, 200) 
    randomtwo = random.randint(-200, 200) 
    draw_triangle(randomone, randomtwo, 100) 
    forward(100) 
    left(120)


def draw_triangle2(x, y, size):
# penup() 
    goto(y, x) 
    # pendown() 
    for i in range(3): 
        forward(size) 
        left(120) 
        color('light pink')
for i in range(7):
        
    # draw a triangle at a random location 
    randomone = random.randint(-200, 200) 
    randomtwo = random.randint(-200, 200) 
    draw_triangle2(randomone, randomtwo, 200)
    forward(100) 
    left(120) 


def draw_triangle3(x, y, size):
# penup() 
    goto(y, x) 
    # pendown() 
    for i in range(3): 
        backward(size) 
        left(120) 
        color('navy')
# draw a bunch of triangles
for i in range(7):
        
    # draw a triangle at a random location 
    randomone = random.randint(-200, 200) 
    randomtwo = random.randint(-200, 200) 
    draw_triangle3(randomone, randomtwo, 300)
    forward(100) 
    left(120) 
    
        
exitonclick()