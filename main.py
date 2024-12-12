a = input("정수를 하나 입력해주세요 ")
print("입력하신 정수는 {} 입니다. ".format(a))
b = input("다른 정수를 하나만 더 입력해주세요")
print("입력하신 정수는 {} 입니다. ".format(b))
print("--------")
try:
    int(a)
    int(b)

    print("a+b= {}".format(a+b))


except Valueerror as exception:
    print("정수를 입력해주라고요.. 제발.. 다시 프로그램을 시작해주세요..")

    


