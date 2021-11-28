mylist = ['a', 'b', 'c', 'd']
print('before')
print(mylist)

mylist[0] = 'NEW ITEM'
print('after')
print(mylist)

mylist.append('NEW')
print(mylist)
# result at end

mylist.append(['f', 'g'])
print(mylist)
# ['NEW ITEM', 'b', 'c', 'd', 'NEW', ['f', 'g']]

listwo = ['f', 'g']
mylist.extend(listwo)
print(mylist)

# pop
item = mylist.pop(0)
print(mylist)
print(item)

# reverse 反向排序
mylist.reverse()
print(mylist)

# sort
listthree = [7, 10, 4, 58]
listthree.sort()
print(listthree)

####
martix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_col = [row[0] for row in martix]
print(first_col)