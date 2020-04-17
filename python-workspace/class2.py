# class2.py

class Unit:
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    def Attack(self, target):   # 클래스의 모든 함수는 첫번째 매개변수로 self를 가져야만 합니다
        target.hp -= self.atk
        print('{}가 {}를 공격하여 {}만큼 데미지를 입혔습니다'.format(self.name, target.name, self.atk))

marine = Unit('마린', 5, 40)
zealot = Unit('광전사', 16, 80)

while True:
    marine.Attack(zealot)
    zealot.Attack(marine)
    print('마린 : {}, 광전사 : {}'.format(marine.hp, zealot.hp))
    if marine.hp < 0:
        print('마린이 졌습니다')
        break
    if zealot.hp < 0:
        print('광전사가 졌습니다')
        break




