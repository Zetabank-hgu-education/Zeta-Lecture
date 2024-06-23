#3-1
customer = "토르"
index = 5

while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))    
    index -= 1 
    if index == 0:
        print("커피는 폐기처분되었습니다.")
        
#3-2 
i = 0
result1 = 0
while i < 100:
    i = i + 1
    if i % 2 == 0:
        result1 = result1 + i
print('1번 방법 : {0}'.format(result1))
        
        