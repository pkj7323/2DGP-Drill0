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
def drunken_move():
    turtle.setheading(random.randint(0, 360))  # 방향 바꾸기
    turtle.forward(random.randint(50, 300))  # 이동
    turtle.stamp()  # 스탬프 찍기
def restart():
    turtle.reset()
turtle.shape('turtle')

turtle.onkey(drunken_move,' ')
turtle.onkey(restart,'Escape')
turtle.listen()

turtle.exitonclick()
