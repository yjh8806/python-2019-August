# ex09_student.py

std = {}
# dict 를 생성
print(type(std))

std.__setitem__('강지원', 17)
std.__setitem__('김혜린', 17)
std.__setitem__('유우진', 17)
std.__setitem__('박준호', 16)

std.pop('김혜린')   # 삭제 이후

find = input('검색할 학생의 이름 입력 : ')

result = std.get(find)

msg = '{}의 나이는 {}살입니다'.format(find, result)
err = '검색결과가 없습니다'

print((result != None) and msg or err)

ob1 = []    # 리스트, 순번으로 데이터를 저장
ob2 = ()    # 튜플, 고정된 데이터
ob3 = {}    # 딕셔너리, key와 value로 저장

print('type(ob1) :', type(ob1))
print('type(ob2) :', type(ob2))
print('type(ob3) :', type(ob3))

ob4 = {
    '손우승' : 16,
    '이재현' : 16,
    '박규림' : 19,   
    '송민경' : 14,
}

for i in ob4:
    print(i, ob4.get(i))

print('std :', std)
print('ob4 :', ob4)