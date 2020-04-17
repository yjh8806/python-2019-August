# ex05_list.py

# List : 여러 데이터를 묶어서 관리하는 자료형, 순번으로 데이터 관리

fruits = ['사과', '바나나', '복숭아', '수박', '딸기', 100]

print(fruits[0])
print(fruits[1])
print(fruits)

for i in fruits:        # fruits 안의 각각의 원소를 i라고 할때
    print(i)            # i의 값을 출력

# 리스트 안에서 원하는 값 검색하기

find = input('검색할 단어를 입력 : ')      # 검색어를 입력받고
flag = False            # 검색되었는지 성공 여부를 저장하는 변수
for i in fruits:        # 리스트 전체에서
    if find == i:       # 검색어와 값이 일치하면
        print(i,'를 찾았습니다')    # 찾았다라고 출력하고
        flag = True                 # 성공 여부를 True로 변경
if flag == False:               # 전체 반복이 끝났음에도 여전히 False이면
    print(find,'를 찾을 수 없습니다')   # 못찾았다라고 출력한다
        
