'''
    프로그래밍은 데이터를 입력 -> 가공 -> 출력 (화면 or 파일) 하는 과정

    변수 : 메모리 공간에 일정 데이터를 저장, 값이 변경될 수 있다
    상수 : 변경할 수 없는 값, 프로그램 시작전 미리 준비되는 값
    함수 : 함수의 반환값이 데이터 역할, 원하는 데이터를 준비하는 코드

    y = f(x)

    반환값 함수이름(매개변수)       파이썬의 함수 정의는 반환값이 생략되어 있다

'''

# 1. 입력받은 정수를 거꾸로 뒤집는 코드 (함수 X)
var1 = '1234'
var1 = input('정수 입력 : ')    # input()은 사용자에게 키보드로 입력받아서, 문자열로 반환
var1 = int(var1)

var2 = 0

while True:
    var2 += var1 % 10
    var2 *= 10
    var1 //= 10
    if var1 < 10:
        var2 += var1
        break

print('var2 :', var2)

# 위 코드를 Reverse() 함수로 정의하기 (매개변수 전달받고, 정수 반환하기)
def Reverse(num): 
    result = 0
    # 숫자를 뒤집는 코드
    while True:
        result += num % 10
        result *= 10
        num //= 10
        if num < 10:
            result += num
            break
    return result

var3 = int(input('다른 정수 입력 : '))
var4 = Reverse(var3)

print('var4 :', var4)

