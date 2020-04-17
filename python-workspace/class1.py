# class1.py

class Member:
    # 회원 정보는 항상 일정한 값을 가지므로,
    # 회원 정보를 저장하는 자료형을 직접 만들면
    # 복잡한 자료형을 쓰지 않아도 회원정보를 하나의 변수로
    # 쉽게 관리할 수 있다

    # name = ''     # 자료형에 저장되는 변수 (클래스 변수)
    # age = 0

    def __init__(self, name, age):  # Initializer : 객체의 속성값의 초기값을 지정
        self.name = name    # 객체에 저장되는 변수 (객체 변수)
        self.age = age
'''
m1 = Member()
m1.name = '이지은'
m1.age = 27

m2 = Member()
m2.name = '홍진호'
m2.age = 37
'''
m1 = Member('이지은', 27)
m2 = Member('홍진호', 37)

print('{}의 나이는 {}살입니다'.format(m1.name, m1.age))
print('{}의 나이는 {}살입니다'.format(m2.name, m2.age))





