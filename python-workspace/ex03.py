# 1. 두 수를 전달받아서 큰 수를 반환하는 함수 Big(n1, n2) 작성
def Big(n1, n2):
    '''
    if n1 > n2:
        return n1
    else:
        return n2
    '''
    return (n1 > n2) and n1 or n2

n1 = int(input('정수1 입력 : '))
n2 = int(input('정수2 입력 : '))
print('{}와 {}중 큰 수는 {}입니다'.format(n1, n2, Big(n1, n2)))

# 2. 생년월일 6자리를 입력받아서, yyyy-mm-dd의 형식 문자열로 반환하는
#    함수 getBirth(num) 작성
def getBirth(num):  # [함수의 정의] 
    # num : 입력정보를 전달받는 매개변수
    result = ''     # 반환할 결과를 저장할 변수 result
    if int(num[:2]) > 19:
        result += '19' + num[:2] + '년 '    # 88년도, 2088? (X)
    else:
        result += '20' + num[:2] + '년 '

    # 월 일을 문자열에 채워넣기 (연도를 2자리에서 4자리로 변경)
    result += num[2:4] + '월 '
    result += num[4:] + '일 '
    return result       # [함수의 반환값]

birth = input('생년월일 6자리 입력 : ')
print('생년월일 :', getBirth(birth))    # [함수 호출]


