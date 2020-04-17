# ex10_member.py

# dict와 list를 활용하여 회원정보를 관리하는 프로그램을 작성

# key값은 userid
# value는 list자료형으로 구성
# list는 순서대로 userpw, username, age, gender, pnum 을 저장한다

from os import system
from getpass import getpass

member = {} # dict
member.__setitem__('iu930516', ['iu', '이지은', '27', '여성', '010-1111-1111'])
member.__setitem__('yellow', ['kong', '홍진호', '37', '남성', '010-2222-2222'])
menu = -1
session = None  # 로그인된 계정을 저장할 변수
system('COLOR 3F')

while menu != 0:
    system('cls')
    # print(member.get('iu930516'))
    # print(member['iu930516'])
    
    # dict의 key는 list의 index와 같은 역할이다


    print('\n=== Dict를 활용한 회원 관리 프로그램 ===\n')
    print('1. 회원가입')
    print('2. 회원검색')
    print('3. {}'.format(session and (session + ' 로그아웃') or '로그인'))
    print('4. 회원탈퇴')
    print('0. 프로그램 종료')
    print('=' * 40)
    
    menu = int(input('메뉴 입력 : '))
    
    # 회원 가입
    if menu == 1:       
        print('\n\t== 회원가입 ==\n')
        userid = input('ID 입력 : ')        # 필요한 정보를 입력받고
        # ID 중복 체크

        userpw = getpass('PW 입력 : ')
        # pw를 재입력받아서 두개의 비밀번호가 서로 일치하는지 검사

        username = input('이름 입력 : ')
        age = input('나이 입력 : ')
        gender = input('성별 입력 : ')
        pnum = input('전화번호 입력 : ')

        info = [userpw, username, age, gender, pnum]
        # 정보를 리스트로 묶어주고

        member.__setitem__(userid, info)
        # ID를 key로, info를 value로 추가
        
        print(member)
        system('pause')

        
    # 회원 검색        
    elif menu == 2:  
        find = input('검색할 ID 입력 : ')
        info = member.get(find)
        # 사용법은 둘다 가능하지만, 함수를 쓰면 없을 경우 None이 된다
        
        if info != None:
            print('ID :', find)
            print('PW : ********')
            print('이름 :', info[1])
            print('나이 :', info[2])
            print('성별 :', info[3])
            print('전화번호 :', info[4])
        else:
            print('결과를 찾을 수 없습니다')

        system('pause')
    
    # 로그인
    elif menu == 3:  
        if session == None:     # 세션에 정보가 없으면 로그인
            id = input('ID : ')
            pw = getpass('PW : ')

            if member.get(id) != None:
                if pw == member.get(id)[0]:
                    print('{}님 로그인 되었습니다'.format(member.get(id)[1]))
                    session = id
                else:
                    print('비밀번호가 일치하지 않습니다')
            else:
                print('계정을 찾을 수 없습니다')
        else:           # 세션에 정보가 있으면 로그아웃
            print('로그아웃 되었습니다')
            session = None
        
        system('pause')
    
    # 회원탈퇴
    elif menu == 4:  
        if session:
            id = session
        else:
            id = input('탈퇴할 ID 입력 : ')
        info = member.get(id)
        
        if info:
            print('{} 계정의 정보를 삭제하려면 비밀번호를 입력하세요'.format(id))
            pw = getpass('{} 계정의 비밀번호 : '.format(id))
        else:
            print('일치하는 ID가 없습니다')  
            system('pause')
            continue          

        if pw == info[0]:
            member.pop(id)
            print('정보가 삭제되었습니다')
            session = None  # 회원 탈퇴 이후 자동 로그아웃
        else:
            print('비밀번호가 일치하지 않습니다')
        system('pause')

    elif menu == 0:
        system('COLOR') 
        # 콘솔창의 색상을 원래대로 돌려놓기

        

    
