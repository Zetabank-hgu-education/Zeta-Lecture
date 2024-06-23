# 1-1 리스트
subway = ["유재석", "조세호", "박명수"]

#append는 맨뒤에 추가 하는 기능
subway.append("하하") 
print(subway)
#조세호씨가 몇번째 칸에 타고 있는가?
print(subway.index("조세호"))
#정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

#1-2 
subway = ["유재석", "조세호", "박명수"]

print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#1-3
num_list = [5,2,4,3,1]
num_list.sort() 
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

#1-4
mix_list = ["조세호", 20, True]
print(mix_list)

mix_list = ["조세호", 20, True]
num_list = [5,2,4,3,1]

num_list.extend(mix_list)
print(num_list)
