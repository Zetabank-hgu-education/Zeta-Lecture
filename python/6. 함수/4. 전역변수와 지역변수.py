#4-1
a= 10

def func():
    a = 20
    print(f"2. {a}")
    return a + 100 
print(f"1. {a}")
print(f"3. {func()}")

#4-2
gun = 10

def checkpoint(soldiers):# 군인수를 전달값으로 받음
    gun = 20    
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

#4-3
gun = 10

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers  
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun 
        
print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2) 
print("남은 총 : {0}".format(gun))

