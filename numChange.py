def out(a):
    print("2진수로 ", bin(a), "입니다.")
    print("8진수로 ", oct(a), "입니다.")
    print("10진수로 ", a, "입니다.")
    print("16진수로 ", hex(a), "입니다.")

while True:
    try:
        number = int(input("진수를 선택하세요(2/8/10/16):"))
        if number == 2:
            n = int(input("2진수로 숫자를 입력하세요: "), 2)
            out(n)
        
        elif number == 8:
            n = int(input("8진수로 숫자를 입력하세요: "), 8)
            out(n)

        elif number == 10:
            n = int(input("10진수로 숫자를 입력하세요: "))
            out(n)

        elif number == 16:
            n = int(input("16진수로 숫자를 입력하세요: "),16)
            out(n)
    except:
        print("숫자입력해")



