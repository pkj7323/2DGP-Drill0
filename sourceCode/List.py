from unittest.util import unorderable_list_difference

twice = ['momo','sana','zwi']
print(type(twice))
print(len(twice))
twice.append('jihyo')
print(twice)
twice.sort()
print(twice)#알파벳 갯수로 소팅
print(twice[0])
print(twice[-1])

black_pink = ['jisu','jeni','rose']
print(len(black_pink))
unite = black_pink + twice #합병한 걸그룹
print(type(unite))
unite.sort()
print(unite[0])
best=unite[:3]
print(best)
low3=unite[-3:]
print(low3)
#게임을 만들 때 여러 개체를 다룰 때 리스트를 사용해야 할것이다.
unite.remove('momo')
unite.insert(0,'pkj')
print(unite)
del unite[-1]
print(unite)