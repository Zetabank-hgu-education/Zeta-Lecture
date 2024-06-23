#2-1
for waiting_no in [0, 1, 2, 3, 4]:
    print(waiting_no)

#2-2
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))
    
for waiting_no in range(5): 
    print("대기번호 : {0}".format(waiting_no))
    
for waiting_no in range(0, 5): 
    print("대기번호 : {0}".format(waiting_no))
    
#2-3
students1 = ["Iron man", "Thor", "I am groot"]
students1 = [len(i) for i in students1]
print(students1)
students2 = ["Iron man", "Thor", "I am groot"]
students2 = [i.upper() for i in students2]
print(students2)