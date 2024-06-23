# 2-1
cabinet = {3:"유재석", 100:"김태호"} 

print(cabinet[3])
print(cabinet[100])  

print(cabinet.get(3))
print(cabinet.get(100))

#2-2
cabinet = {3:"유재석", 100:"김태호"} 
print(cabinet[5])
print("hi")

cabinet = {3:"유재석", 100:"김태호"} 
print(cabinet.get(5))
print("hi")

#2-3
cabinet = {3:"유재석", 100:"김태호"} 

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

#2-4
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])


cabinet["C-20"] = "조세호"
cabinet["A-3"] = "김종국"
print(cabinet)

#2-5
cabinet = {"A-3":"유재석", "A-100":"김태호"} 
print("A-3" in cabinet)
print("A-5" in cabinet)

del cabinet["A-3"]
print(cabinet)

cabinet.clear()
print(cabinet)




