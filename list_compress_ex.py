import itertools

lst = ['aaa','bbbb','cccc','ddd']
lst1 = [1,0,1,1]

compresed_list = itertools.compress(lst,lst1)
print(list(compresed_list))

# accumulate
# chain

