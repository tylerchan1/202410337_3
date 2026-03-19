def pp(a):
    print("2진수로 ", bin(a), "입니다.")
    print("8진수로 ", oct(a), "입니다.")
    print("10진수로 ", a, "입니다.")
    print("16진수로 ", hex(a), "입니다.")
    
number = int(input("진수를 선택하세요(2/8/10/16):"))
if number == 2:
    n = int(input("2진수로 숫자를 입력하세요: "), 2)
    pp(n) #1010 = 10
elif number == 8:
    n = int(input("8진수로 숫자를 입력하세요: "), 8)
    pp(n) # Oo12 = 10

elif number == 10:
    n = int(input("10진수로 숫자를 입력하세요: "))
    pp(n) # 10

elif number == 16:
    n = int(input("16진수로 숫자를 입력하세요: "),16)
    pp(n) #OxA