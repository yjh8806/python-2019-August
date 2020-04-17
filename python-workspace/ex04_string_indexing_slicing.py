# ex04_string_indexing_slicing.py
# 문자열의 인덱싱(순번 매기기)과 슬라이싱(문자열의 일부 잘라내기)

''' 모든 문자열은 각 글자마다 순번(index)를 가지며, 그 값은 항상 0부터 시작'''

str1 = 'ITBANK'

print(str1[0])  # 문자열의 순번을 표기할 때는 [] 안에 숫자를 기재한다

print(str1[3])  # A를 출력하기 위해서, 0부터 1,2,3 세어서 순번에 3을 기재

print(str1[-3]) # A를 출력하기 위해서, -1부터, -2, -3 세어서 순번에 -3을 기재

# 문자열의 슬라이싱 : 시작점과 끝점을 지정하면 (끝점 포함하지 않음) 문자열을 잘라낸다

print(str1[0:2])    # 0부터 2이전까지 잘라낸다
print(str1[2:4])
print(str1[4:6])

# str2의 내용을 year, month, date, dayofweek 에 따로 담으세요
str2 = '20190714Sunday'

year = str2[0:4]
month = str2[4:6]
date = str2[6:8]
dayofweek = str2[8:]

print(year, month, date, dayofweek)
