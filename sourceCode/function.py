def add(a,b):
    return a+b
def mul(a,b):
    return a*b

#파이썬은 연산자 오버로딩이 되어있다. 대표적인 것이 + 연산자 int는 더하고 string은 합친다.
result = add(2,3)
print(result)

#다중 대입도 가능하다.
a = 100
b = 1
a, b = b, a
print((a,b))

def sum_and_mul (x,y):
    return x+y,x*y
a = sum_and_mul(1,2)
print(a)

_ , b = sum_and_mul(1,2)#받기 싫으면 언더바로 처리하면된다.
print(b)
