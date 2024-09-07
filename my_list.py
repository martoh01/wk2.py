my_list = [10, 20, 30, 40]
my_list.insert(1, 15)
my_list.extend([50, 60, 70])

last_element = my_list.pop()
#print(last_element)
#print(my_list)
my_list.sort()
index_30 = my_list.index(30)
print(index_30)