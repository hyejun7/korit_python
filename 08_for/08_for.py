word = "python"

for char in word:
    print(char)

for i in range(5):
    print(i)

for i in range(2, 10, 2): #2부터 10 미만까지, 2씩 증가
    print(i)

for i in range(1, 10):
    print(i)
    if i == 5:
        print("i가 5입니다. 정지!")
        break

for num in range(1, 10):
    if num == 5:
        continue
    print(num)

#실습 문제
#1부터 100까지 짝수만 출력하기(range)
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)

for i in range(2, 101, 2):
    print(i)

#리스트의 합 구하기
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("리스트의 합:", total)


for dan in range(1, 10):
    for n in range(1, 10):
        print(f"{dan} x {n} = {dan * n}")

#평균 구하기
scores = [80, 90, 75, 88, 92]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print("평균 점수:", average)
