# 이름과 나이를 입력받아서, 화면에 한줄로 출력하는 함수를 제작하세요

def ShowNameAge(name, age):
    # 전달받은 이름과 나이를 출력하는 코드
    str1 = '{}님의 나이는 {}살입니다'.format(name, age)
    print('%s님의 나이는 %d살입니다' % (name, age))
    print(str1)
    return str1

# 사용자에게 이름과 나이를 입력받고, 함수를 호출하면서 인자를 전달하는 코드
name = input('이름 입력 : ')
age = int(input('나이 입력 : '))

ShowNameAge(name, age)
print(ShowNameAge(name, age).index('2'))
print('12345'.index('2'))
'''
    프로그래밍 언어에서 사용되는 [값, data]의 종류

    변수 : 데이터를 담기 위한 메모리 공간, 값이 변경될 수 있다. 자료형을 동반한다
    함수 : 값을 구하기 위한 일정한 수식, 코드의 묶음
    상수 : 프로그램 시작전에 미리 준비된 값, 값을 변경할 수 없다

    파이썬은 클래스를 지원하는 언어이므로, 
    모든 값에 .을 붙여서 소속된 기능을 호출할 수 있다

'''