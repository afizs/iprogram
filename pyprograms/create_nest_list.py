__author__ = 'Afiz'
from pprint import pprint
file = open('data_for_n_list.txt', 'r')
data = file.readlines()
print(len(data))
main_list = []
for i in range(0, len(data), 3):
    child_list =[]
    child_list.append(data[i].strip())
    child_list.append(data[i+1].strip())
    child_list.append(data[i+2].strip())
    main_list.append(child_list)

pprint(main_list)
