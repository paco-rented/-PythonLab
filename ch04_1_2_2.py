numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number >= 100 :
        print(number, "는 3자릿수입니다")
    elif number >= 10 :
        print(number, "는 2자릿수입니다")
    else :
        print(number, "는 1자릿수입니다")