
"""
x = 3
print(str(x))
print(float(x))

y = 7.54
print(int(y))

print(x + y)
print(x - y)
print(x / y)
print(x // y)
print(round(y))

A = [60, 70, 10, 20, 81, 63, 4]
print(A[2])
print(A[0:6])
print(A[1:5])
print(A[-5])
"""
"""
import math
x = math.sqrt(36)
print(x)
"""
"""
y = 4
print((y/2)*(y/2)*3.14)

x = [10, 30, 40, 90, 100, 61]
print(sum(x)/len(x))
print(round(55.1666666666664))
"""
"""
score = 55

if score >= 60:
    print("及格了")
else:
    print("被當了")
"""
"""
score = 51
if score >=60:
    print("及格了")
elif 55 <= score or score < 60:
    print("教授拜託調分")
elif 50 <= score < 55:
    print("差一點點")
else:
    print("被當了")
"""
"""
score = 98
if score >=60:
    print("及格了")
    if score >= 90:
        print("你最棒了")
        if score >= 95:
            print("你超屌")
elif 55 <= score <60:
    print("教授拜託調分吧")
else:
    print("被當了")
"""
"""
print("Hello world")
print("Hello")
print("Hello", "world", "!")
print("123", end=" ")
print("456")
"""
"""
x = 42
print(f"Value of x is {x}")

mathScores = [60, 70, 10, 20, 81, 63, 4]
print(mathScores[0])
firstItem = f"first item in mathScores is {mathScores[5]}"
print(firstItem)
print(f"the mathScores has {len(mathSocres)} items")
"""
"""
for i in range(0, 10):
    print(i)

for x in range(10):
    print(x)

for z in range(0, 15, 3):
    print(z)
"""
"""
Scores = [60, 70, 10, 20, 81, 63, 4]
len_Scores = len(Scores)
for i in range(len_Scores):
    print(i, Scores[i])


Scores = [60, 70, 10, 20, 81, 63, 4]
for item in Scores:
    print(item)
"""
"""
family = {"dad": "Homer",
          "mom": "Marge",
          "son": "Bart",
          "daughter": "Lisa"
}
for member in family.items():
    print(member)
for gg, yy in family.items():
    print(f'my {gg} is {yy}')
"""
"""
練習
import
mathScores = [60, 70, 10, 20, 81, 63, 4]
for score in mathScores:
    print(math.sqrt(score) * 10)
"""
"""
進階1
for i in range(10):
    print(i)
[print(i) for i in range(10)]
"""
"""
進階2
import math
mathScores = [60, 70, 10, 20, 81, 63, 4]
for item in mathScores:
    print(math.sqrt(item) * 10)

[print(math.sqrt(item) * 10) for item in mathScores]
"""
"""
count = 0
while count < 10:
    print(count)
    count += 1

count = 0
while count < 10:
    print(count)
    count +=1
else:
    print("loop end")
"""
"""
mathScores = [60, 70, 10, 20, 81, 63, 4]
for score in mathScores:
    if score >80:
        break
    print(score)
"""
"""
mathScores = [60, 70, 10, 20, 81, 63, 4]
for score in mathScores:
    if score >80:
        continue
    print(score)
"""
"""練習題1
for a in range(1,10):
    for b in range(1,10):
        print(f"{a} * {b}=",a*b )
2
count = 0
while count <51:
    print("你好")
    count += 1
else:
    print("我說完啦")
"""

"""
3
num = eval(input('Enter a number: '))
for i in range(1, num+1):
    if i % 2 == 1:
        print(i)
"""
"""
class Student:
    def _init_(self):
"""
studentB = "I am studentB"
print(studentB)
