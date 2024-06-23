#비밀번호를 만들어주는 프로그램 작성

# 예) url = "http://naver.com"
#규칙1 : url 변수에서 http:// 부분은 제외 => naver.com    / replace함수 이용
#규칙2 : 규칙1 결과값에서 처음 만나는 점(.) 이후 부분은 제외 => naver
#규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!"로 구성
              #(nav)               (5)            (1)             (!)
# 예) 생성된 비밀번호 : nav51!
# password 변수를 이용하여 비밀번호 도출
#규칙4 : format함수를 이용하여 "url의 password는 입니다" 도출     

url = "http://naver.com"
my_str = url.replace("http://", "")
#print(my_str)
my_str = my_str[:my_str.index(".")]
#print(my_str)    
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
#print(password)
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))


