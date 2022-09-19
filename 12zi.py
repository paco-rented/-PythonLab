str_input = input("태어난 해를 입력해 주세요> ")
birth_year = int(str_input) % 12
# 나머지를 기준으로 연산을 한 거인데...변수를 지정할 때 이미 연산을 끝내버리면 굳이 조건문에서 연산을 반복할 필요가 없음

if birth_year == 0:
    print("원숭이 띠입니다")
elif birth_year == 1:
    print("닭 띠입니다")
elif birth_year == 2 :
    print("개 띠입니다")
elif birth_year == 3 :
    print("돼지 띠입니다")
elif birth_year == 4 :
    print("쥐 띠입니다")
elif birth_year == 5 :
    print("소 띠입니다")
elif birth_year == 6 :
    print("범 띠입니다")
elif birth_year == 7 :
    print("토끼 띠입니다")
elif birth_year == 8 :
    print("용 띠입니다")
elif birth_year == 9 :
    print("뱀 띠입니다")
elif birth_year == 10 :
    print("말 띠입니다")
elif birth_year == 11:
    print("양 띠입니다")