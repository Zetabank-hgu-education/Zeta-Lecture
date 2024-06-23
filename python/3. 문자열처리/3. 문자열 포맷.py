# 3-1 문자열 포맷
print("나는 %d살입니다." % 20) 
print("나는 %s을 좋아해요"% "파이썬")
print("Apple 은 %c로 시작해요" %"A") 

print("나는 %s살 입니다"% 20) 
print("나는 %s색과 %s색을 좋아해요"% ("파란", "빨간"))

# 3-2 format method
print ("나는 {}살입니다.".format(20)) 
print ("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) 
print ("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) 
print ("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))

print("a" + "b") #이와같이 사용하면 ab가 붙어서나옴
print("a", "b") #콤마를 이용하면 a와 b가 띄어져서 나옴

# 3-3 F-string
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

animal = "고양이"
name = "까망이"
print(f"내가 키우는 애완견은 {animal}고, 이름은 {name}에요")












 