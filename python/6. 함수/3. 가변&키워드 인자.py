#3-1
def multi_sum(*args):
    num = len(args)
    print("입력 된 변수 개수 : ", str(num)+"개")
    print(args)
    
multi_sum(1,2,3,4,5,6,7)
multi_sum(5,1,3,2)

#3-2
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end="")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "Jave", "C", "C++", "C#", "JavaScript")
profile("김태호", 20, "kotlin", "swift",)

#3-3
def kwargs_func(**kwargs):
    print(kwargs)
    
kwargs_func(a=1, b=2, c=3)
kwargs_func(fruit = '사과', vegitable = '배추')

#3-4
def kwargs_func(**kwargs):   
    for v in kwargs.keys(): 
        print("{}".format(v), kwargs[v])
        print('-----')
        
kwargs_func(name1='Lee', name2='Park', name3='Cho')