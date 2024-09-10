import turtle
import random

'''
import turtle
turtle.setheading(90)#윗쪽
turtle.setheading(0)#오른쪽
turtle.setheading(180)#왼쪽
turtle.setheading(-90)#아래쪽
turtle.setheading(360)#오른쪽
turtle.exitonclick()
'''
turtle.shape('turtle')
while (True):
    turtle.setheading(random.randint(0,60))#방향 바꾸기
    turtle.forward(random.randint(0,100))#이동
    turtle.stamp()#스탬프 찍기
