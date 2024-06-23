#4-1
set1 = {1,2,3,3,3}
print(set1)
set2 = set({2,3,3,1,5})
print(set2)

#4-2
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python)
print(java.intersection(python))

print(java | python)
print(java.union(python))

print(java - python)
print(java.difference(python))

#4-3 자료구조비교
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

#4-4
menu = ["커피", "우유", "주스"]
menu_dict = {index: item for index, item in enumerate(menu)}
print(menu_dict)

menu = ["커피", "우유", "주스"]
flavor = ["커피", "딸기", "오렌지"]

menu_flavor_dict = dict(zip(menu, flavor))
print(menu_flavor_dict)






