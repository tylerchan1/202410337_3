calcChoice = input("1.입력한 수식 계산 2.두 수 사이의 합계 : ")

if(calcChoice == '1'):
    mod = input("*** 수식을 입력하세요: ")
    print(mod, " 결과는 ", eval(mod), "입니다.")

else:
    number1 = int(input("*** 첫 번째 숫자를 입력하세요: "))
    number2 = int(input("*** 두 번째 숫자를 입력하세요: "))
    result = 0
    for i in range(number1, number2+1):
        result =+ i
        print(i)

    print(number1,"+...+", number2,"는", result, "입니다.")