import turtle
import random

turtle.shape('turtle')
while (True):
    turtle.setheading(random.randint(0,360))#방향 바꾸기
    turtle.forward(random.randint(0,100))#이동
    turtle.stamp()#스탬프 찍기
