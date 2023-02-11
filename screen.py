import random
import turtle
import time
t = turtle.Turtle()
t.speed(1000) 
turtle.Screen().bgcolor("black")
t.color("white")   
t.pensize(2)     


colors = ['crimson', 'medium slate blue']

for i in range(6):
    t.penup()
    t.goto(-600, 175 - i * 75)
    t.pendown()
    t.circle(20)
    t.write(f"X{i + 1}")

# Draw the hidden layer nodes
for i in range(12):
    t.penup()
    t.goto(-300, 275 - i * 55) 
    t.pendown()
    t.circle(20)
    t.write(f"H{i + 1}")

# Draw the hidden layer nodes
for i in range(14):
    t.penup()
    t.goto(0, 320 - i * 55)  
    t.pendown()
    t.circle(20)
    t.write(f"H{i + 1}")

# Draw the hidden layer nodes
for i in range(8):
    t.penup()
    t.goto(300, 200 - i * 65)  
    t.pendown()
    t.circle(20)
    t.write(f"H{i + 1}")


# Draw the output layer node
for i in range(4):
    t.penup()
    t.goto(600, 130 - i * 100)
    t.pendown()
    t.circle(20)
    t.write("Y")


while True: 
    for i in range(6):
        for j in range(12):
            t.pencolor(random.choice(colors))  # change the color randomly
            t.penup()
            t.goto(-600, (175 - i * 75)+20)
            t.pendown()
            t.goto(-300, (275 - j * 55)+20)


    for i in range(12):
        for j in range(14):
            t.pencolor(random.choice(colors))  # change the color randomly
            t.penup()
            t.goto(-300, (275 - i * 55)+20)
            t.pendown()
            t.goto(0, (320 - j * 55)+20)


    for i in range(14):
        for j in range(8):
            t.pencolor(random.choice(colors))  # change the color randomly
            t.penup()
            t.goto(0, (320 - i * 55)+20)
            t.pendown()
            t.goto(300, (200 - j * 65)+20)


    for i in range(8):
        for j in range(4):
            t.pencolor(random.choice(colors))  # change the color randomly
            t.penup()
            t.goto(300, (200 - i * 65)+20)
            t.pendown()
            t.goto(600, (130 - j * 100)+20)


turtle.done()


