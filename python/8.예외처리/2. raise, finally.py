#2-1 raise
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 :"))
    num2 = int(input("두 번째 숫자를 입력하세요 :"))
    if num1 >= 10 or num2 >= 10: # num1, num2가 두자리숫자일때 에러발생
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


#2-2

class BigNumberError(Exception): #exception이라는 클래스를 상속받음
    pass
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 :"))
    num2 = int(input("두 번째 숫자를 입력하세요 :"))
    if num1 >= 10 or num2 >= 10: # num1, num2가 두자리숫자일때 에러발생
        raise BigNumberError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. ")
except BigNumberError:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")

#2-3 
class BigNumberError(Exception): #exception이라는 클래스를 상속받음
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 :"))
    num2 = int(input("두 번째 숫자를 입력하세요 :"))
    if num1 >= 10 or num2 >= 10: # num1, num2가 두자리숫자일때 에러발생
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)

#2-4 finally
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("첫 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2))) 
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
finally:
    print("계산기를 이용해 주셔서 감사합니다.")