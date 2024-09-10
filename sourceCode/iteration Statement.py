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


for v in [1,3,4,5]:
    print(v)
print("\n")
for c in "Park Kyoung Jun":
    print(c)

total = 0
for i in range(1,100 + 1):#range는 1~100까지의 정수를 만들어 낸다.
    total += i
print(total)