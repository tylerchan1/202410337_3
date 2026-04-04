test = (1,2,3,4,5,6)
print(test)# print tuple
print(type(test))# print type of tuple

test1 = (1,)
print(test1)

print(test[2:5])

test2 = test + test1

print(test2)

print(len(test2))

a = 1,2,3 #packing

o, t, th = a #unpacking
#튜플과 언패킹 요소의 수가 일치하여야만 가능

city, latitude, longitude = 'Seoul', 37.54, 126.98

print(city)

print(test2.index(2))
print(test2.count(1))
