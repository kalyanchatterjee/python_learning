my_list = ['apple', 'orange', 'banana']
print(id(my_list))
# adding to the list
print(id(my_list.append('watermelon')))


my_list2 = my_list

print(my_list == my_list2)

print(my_list)
print(my_list2)

text = "abcd"
print(len(text))
