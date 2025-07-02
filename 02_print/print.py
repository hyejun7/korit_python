# 입력받기
#input()
# a = input()
# print("내가 입력한 것 : " + a)
from py import first_name

# username = input("이름을 입력하세요 : ")
# print("사용자 이름 : " + username)

# age = input("나이를 입력하세요 : ")
# print(type(age))
# print("사용자 나이 : " + age)
#input()으로 입력 받은 모든 값은 문자열 형태이다.

#출력하기 다양한 방식
# last_name = "박" #문자열 str
# first_name = "연호"
# neme = last_name + first_name
# age = 21 #int

# print("hi" = "hello"+ "world")
# print("hi", "hello1", "world")
# print("내 전화번호는 " + phone_uvmber + "입니다.")
# print("제 나이는 " + age + "입니다.")
# print("제 나이는 {} 입니다.".format(age))
# print("제 이름은 {}, 나이는 {} 입니다.".format(name, age))
# print("제 이름은 {nm}, 나이는 {ag} 입니다.".format(nm="홍길동", ag=18))

# print(f"제 나이는 {age} 입니다") #f-string 방식

# print("제 나이는 %s 입니다." % age) #모든 문자를 문자열로 포맷팅해서 출력
# print("제 나이는 %d 입니다." % age) #모든 문자를 정수형로 포맷팅해서 출력
# print("제 이름은 %s 이고 제 나이는 %d 입니다." %(neme, age))
# print("Loading...%d%% " % 98)
# print( "%10s" % "hi") #문자열 포함 길이(문자열 앞에 공백 포함)
# print("%-10s" % "hello ") #문자열 포함 길이 (문자열 뒤에 공백포함)



"""
%s => 문자열 
%c => 문자 1개
%d => 정수
%f =>실수
%o =>8진수
%x => 16진수
%% => 리터럴(문자 % 자체)
"""

# 실습
# 이름:
# 나이:
# 취미:
# 주소:
# 각각 변수에 넣고 f-string방식으로 출력
# ex) 제 이름은 ***이고 나이는 **살 입니다. 제 취미는 ***입니다

naem = input("이름 : ")
age = input("나이 : ")
hoddy = input("취미 : ")
address = input("wnth : ")
print(f"제 이름은 {name} 제 나이는 {age}이고  ")