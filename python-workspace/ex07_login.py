# ex07_login.py

import getpass

account = ['itbank', 'root', 'test', 'iu930516']    # 계정
password = ['it', '1', 'test', 'iu']                # 비밀번호
name = ['아이티', '관리자', '테스트', '이지은']       # 사용자 이름

# 계정과 비밀번호를 입력받아서, 계정의 비밀번호가 서로 일치하면
# 사용자의 이름과 환영합니다 메시지를 출력하고
# 로그인에 실패하면, 계정이 없는지, 비밀번호가 틀렸는지, 오류 내용을 출력하세요

flag = False
userid = input('ID : ')
userpw = getpass.getpass('PW : ')

for i in range(len(account)):   # 계정 목록 중에서
    if account[i] == userid:    # 입력받은 계정과 일치하면
        flag = True             # 계정 찾았음
        if password[i] == userpw:   # 비밀번호가 일치하면
            print('{}님, 환영합니다'.format(name[i]))   # 환영 메시지 출력
            break               # 원하는 계정을 찾았으므로, 반복 중단
        else:                       # 비밀번호가 일치하지 않으면
            print('비밀번호를 다시 확인해주세요')
            break

if flag == False:       # for문이 끝났지만, 계정을 못 찾았다면
    print('계정을 다시 확인해주세요')



'''
data1 = input('ID : ')
data2 = getpass.getpass('PW : ')

print(data1, data2)
'''

'''
    1. 변수와 자료형 (str, int, float, bool)
    2. 연산자 (대입, 논리, 산술, 크기비교, 삼항연산)
    3. 제어문 (if, while, for, break)
    4. 함수 (정의, 선언, 호출, 매개변수)
    5. 문자열 (indexing, slicing, len())
    6. 확장 자료형 (list, tuple, dictionary)
'''