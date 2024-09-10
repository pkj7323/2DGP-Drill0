'''
import turtle

while True:
    shape=input("Enter a shape: ")
    if shape == "circle":
        turtle.circle(50)
        turtle.exitonclick()
    elif shape == "triangle":
        turtle.forward(50); turtle.left(120)
        turtle.forward(50); turtle.left(120)
        turtle.forward(50)
        turtle.exitonclick()
    elif shape == "quit":
        break
    else:
        print("Invalid input")
turtle.bye()
'''

'''
import turtle
turtle.setheading(90)#윗쪽
turtle.setheading(0)#오른쪽
turtle.setheading(180)#왼쪽
turtle.setheading(-90)#아래쪽
turtle.setheading(360)#오른쪽
turtle.exitonclick()
'''
