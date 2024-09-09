# key와 value 페어로 이루어진 사전형 자료형 map과 같은 것
score = {'momo':80, 'zwi':85, 'sana':98}
print(type(score))
print(score['momo'])#key값으로 인데싱해서 찾으러 갈 수 있다
#print(score['trump'])<-값이 없어서 키오류가난다
score['trump'] = 0
#score.sort()도 안된다. 키페어는 순서가 없기 때문에
print(score.values())#스코어에 저장되어있는 값들만 가져올 수 있다. 일종의 리스트
print(sum([1,2,3,4,5,6,7,8,9,10]))#리스트안에있는 값을 더해주는 함수 sum
print(sum(score.values()))
print(sum(score.values())/len(score))

