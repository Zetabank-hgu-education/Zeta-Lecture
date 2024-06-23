# - 학교에서 파이썬 코딩 대회를 추최합니다. 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자들 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다. 추첨 프로그램을 작성시오.

#  조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
#  조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가 (한명이 치킨받으면 그 사람은 커피는 못받음)
#  조건3 : random 모듈의 shuffle 과 sample을 활용
#  		(당첨자 발표시 출력값)			
#  		   -- 당첨자 발표 --
#  		   치킨 당첨자 : 1 
#  		   커피 당첨자 : [2, 3, 4] 
#  		   -- 축하합니다 --

from random import *
users = range(1,21)
#print(type(users))
users = list(users)
#print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) #4명 중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")