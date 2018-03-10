from pprint import pprint
__author__ = 'Afiz'

file = open('data_for_n_list.txt', 'r')
data = file.readlines()
print(len(data))

nest_list = []
for i in range(0, len(data), 3):
    child_list = []
    child_list.append(data[i].strip())
    child_list.append(data[i+1].strip())
    child_list.append(data[i+2].strip())
    nest_list.append(child_list)
pprint(nest_list)
