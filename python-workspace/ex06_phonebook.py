# ex06_phonebook.py

phonebook = [
    '원종래','010-9128-3434',
    '홍진호','010-2222-2222',
    '이지은','010-3333-3333',
]

name = input('이름 입력 : ')
num = input('전화번호 입력 : ')

phonebook.append(name)  # 값 추가하는 기능
phonebook.append(num)

print(phonebook)

find = input('검색어 입력 : ')
flag = False

for i in range(len(phonebook)): # phonebook의 길이만큼 반복(횟수)
    if find == phonebook[i]:    # 검색어와 phonebook의 i번째가 일치하면
        flag = True
        if i % 2 == 0:  # 짝수이면 (이름)
            print('%s : %s' % (phonebook[i], phonebook[i + 1]))
        else:       # 짝수가 아니면, 홀수이면 (전화번호)
            print('%s : %s' % (phonebook[i - 1], phonebook[i]))
if flag == False:
    print('%s : 찾을 수 없습니다' % find)








