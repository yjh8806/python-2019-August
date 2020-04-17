# Member의 클래스를 정의 (자료형 만들기)

class Member:

    def __init__(self, userid, userpw, username, birth, gender):
        self.userid = userid
        self.userpw = userpw
        self.username = username
        self.birth = birth
        self.gender = gender
    
    def Show(self):
        print()
        print('계정이름 : {}'.format(self.userid))
        print('비밀번호 : ********')
        print('사용자이름 : {}'.format(self.username))
        if len(self.birth) == 6:
            birth = '{}년 {}월 {}일'.format(self.birth[:2], self.birth[2:4], self.birth[4:])
        else:
            birth = '정확한 정보가 입력되지 않았습니다. 다시 수정해주세요'
        print('생년월일 : {}'.format(birth))
        print('성별 : {}'.format(self.gender))
        print()

class Member2(Member):  # Member의 내용을 모두 물려받은 자식 클래스 Member2
    pass


from os import system           # 운영체제 명령어를 사용하기 위해서
from getpass import getpass     # 비밀번호를 노출하지 않고 입력받기 위해서

memberList = []
menu = 0
memberList.append(Member2('test', '1234', '테스트', '000102', '남성'))
session = None  # 로그인 된 계정을 저장할 변수


while True:
    print('1. 회원가입')
    print('2. 회원검색')
    print('3. {}'.format((session == None) and '로그인' or session.userid + ' 로그아웃'))
    print('4. 회원탈퇴')
    print('5. 프로그램 종료')
    menu = int(input('메뉴 입력 : '))

    if menu == 1:
        # 회원 가입 코드
        userid = input('사용자 계정 입력 : ')
        userpw = getpass('비밀번호 입력 : ')
        username = input('사용자 이름 입력 : ')
        birth = input('생년월일 입력 : ')
        gender = input('성별 입력 : ')

        newMember = Member(userid, userpw, username, birth, gender)
        # 새로운 회원객체를 생성

        memberList.append(newMember)
        # 방금 만든 객체를 리스트에 추가

    elif menu == 2:
        flag = False    # 검색되었는지 여부를 저장하는 변수
        find = input('검색할 ID 입력 : ')   
        for member in memberList:
            if member.userid == find:
                member.Show()
                flag = True # 검색되었으면 True
                break
        if flag == False:
            print('{}를 찾을 수 없습니다'.format(find))

    elif menu == 3:
        if session == None:
            # 로그인
            id = input('ID : ')
            pw = getpass('PW : ')
            flag = False
            for member in memberList:
                if member.userid == id:
                    flag = True
                    if member.userpw == pw:
                        print(member.username, '님 로그인을 환영합니다')
                        session = member
                        break
                    else:
                        print('비밀번호를 다시 확인해주세요')
                        break
            if flag == False:
                print('계정을 찾을 수 없습니다')
        else:
            # 로그아웃 버튼 작동
            print('로그아웃 되었습니다')
            session = None

    elif menu == 4:
        # 회원 탈퇴
        if session != None: # 로그인 된 상태이면
            id = session.userid
        else:               # 로그인 상태가 아니면
            id = input('탈퇴할 ID 입력 : ')
        pw = getpass('{}의 비밀번호를 입력 : '.format(id))
        flag = False

        for i in range(len(memberList)):    
            if memberList[i].userid == id and memberList[i].userpw == pw:
                flag = True
                leave = memberList.pop(i)   # pop() 함수는 입력값으로 index를 넣어야 한다
                print(leave.userid, '계정이 탈퇴처리 되었습니다')
                session = None
                break
        if flag == False:
            print('계정이 존재하지 않습니다')






    elif menu == 5:
        print('프로그램을 종료합니다')
        break







