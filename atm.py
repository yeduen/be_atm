# balance : 통장에 들어있는 기본 금액을 담는 변수
#1.입금, 2.출금, 3.영수증 보기, 4.종료 => 글자를 입력 받을지(입금, 출금 ...) / 숫자를 입력받을지(1,2,3..)
#숫자로 원하는 기능을 입력할 수 있게 만들어주세요ㅕ. 긜고 사용자가 입력한 기능은 num 변수에 담아주세요
# deposit_amount: 

balance = 3000

while True:
    num = input("사용하실 기능을 선택해주세요(1.입금, 2.출금, 3.영수증 보기, 4.종료)")

    if num == "1":
        deposit_amount = input("입금할 금액을 입력해주세요 :") #isdigit() => 문자열을 숫자열로 변경해주는 함수 ex) "123123123" => True
        if deposit_amount.isdigit() and int(deposit_amount) > 0: #첫번째 조건 문자가 입력된건 아닌지 확인 / 0보다 큰 금액을 입력했는지
            balance += int(deposit_amount) #balance = balance + ini(deposit_amount)
            print(f"고객님이 입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.")
        else:
            print("정신차리고, 제대로된 숫자형태로 입금액을 작성해줘^^ㅗ")
    if num == "2":
        pass
    if num == "3":
        pass
    if num == "4":
        print("서비스를 종료합니다.")
        break

