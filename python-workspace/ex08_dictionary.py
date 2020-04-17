# ex08_dictionary.py

'''
사전 (Dictionary) : 데이터를 저장할 때, 배열의 순번 대신, key를 이용하여 데이터들을 저장

다수의 데이터를 이름별로 구분하여 저장할 때 사용하며
key를 알면 value을 알아낼 수 있으나, value만 아는 경우, key를 알아낼 수 없다
'''

student = {}

# dict 자료형에 key, value를 넣기 위해서 __setitem__(key, value) 함수를 사용한다

student.__setitem__('원종래', '연산동')
student.__setitem__('이지은', '서울')
student.__setitem__('김태문', '해운대')

# 학생의 이름을 알고 있다면, 주소를 확인할 수 있다

print(student.get('원종래'))
print(student.get('이지은'))
print()

print('[김태문] 학생의 주소 :', student.get('김태문'))

# 주소를 알고 있다고 해서, 학생의 이름을 확인할 수는 없다

print(student.get('해운대'))

print(student['이지은'])        # 리스트의 인덱스와 같은 역할을 한다
print(student.get('이지은'))    # 함수를 이용해서 호출하면 실수를 줄일 수 있다
#print(student['이지금'])        # Key (인덱스) 위치가 잘못되면 곧바로 오류가 발생
print(student.get('이지금'))    # get함수를 이용하면, 값이 없어도 오류는 발생하지 않고 None값을 반환

result = student.pop('이지은')   # key값을 이용해서 맵핑되어 있는 value를 같이 제거한다 (꺼낸다)

print(student.get('이지은'))
print(result)












