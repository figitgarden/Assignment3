from turtle import *
import random
speed(20)
def draw_triangle(x, y, size): 
# penup() 

    goto(x, y) 
    # pendown() 
    for i in range(3): 
        forward(size) 
        left(120) 
# draw a bunch of triangles
for i in range(9):
        
    # draw a triangle at a random location 
    randomone = random.randint(-200, 200) 
    randomtwo = random.randint(-200, 200) 
    draw_triangle(randomone, randomtwo, 100) 
    forward(100) 
    left(120) 
        
exitonclick()