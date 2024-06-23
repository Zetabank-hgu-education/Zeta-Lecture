# 1-1
def func():
    print('BlockDMast')
func()

# 1-2
def func2(a,b):
    print(f'{a} 곱하기 {b} = {a*b}')
    
func2(1,2)
func2(1,3)
func2(2,4)

#1-3
def func3():
    return "abcdefg"

a = func3()
print(a + "GG")

# 1-4 
def func4(a,b):
    return a*b
c = func4(3,9)
print(c)

#1-5
# 입력도 없고 반환값도 없는 함수
def function1():
    print("예제1 호출")
    
function1()
#입력만 있는 함수
def function2(a,b):
    print("예제2 호출", a,b)
function2(10,20)
#반환값만 있는 함수
def function3():
    return " 예제3 호출"
a = function3()
print("지금" + a)
#입력 반환 둘다 있는 함수
def function4 (x,y):
    return x+y
r = function4(50,50)
print("예제4 호출", r)

#1-6
def open_account(): 
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): 
    print("입금이 완료 되었습니다. 잔액은 {} 원입니다.".format(balance + money)) 
    return balance + money     

def withdraw(balance, money): 
    if balance >= money: 
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance
    
balance = 0     
balance = deposit(balance, 1000) 
print(balance)
balance = withdraw(balance, 500)
print(balance)    

