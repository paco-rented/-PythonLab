conv = input("입력: ")
import datetime
now = datetime.datetime.now()

if "안녕" in conv :
    print("안녕하세요")

elif "몇 시" in conv :
    print("지금은 {}시입니다".format(now.hour))

else :
    print(conv)