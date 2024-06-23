#2-1 문자열 처리 함수
python = "Python is Amazing" 

print(python.lower()) 
print(python.upper()) 
print(python[0].isupper())
print(python[1].isupper())
print(python[0].islower())
print(python[1].islower()) 

# 2-2
python = "Python is Amazing" 

print(len(python)) 
print(python.replace("Python", "Java"))
print(python.count("n")) 

# 2-3
python = "Python is Amazing" 

index = python.index("n") 
print(index) 

index = python.index("n", index + 1) 
print(index)

print(python.find("n"))

# 2-4
#index
python = "Python is Amazing" 

print(python.index("Java")) 
print("hi")
#find
python = "Python is Amazing" 

print(python.find("Java"))
print("hi")













