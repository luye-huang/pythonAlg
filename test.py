for i in range(4, 0, -1):
    print(i)
print([1,2][2:])
aa = [1, 2]
bb = aa.copy()
aa[0] = 5
print(bb)
print(int((1+4)/2))
print(len([1, 2]))
arr =[1,2]
arr[0:0] = [3, 5]
dict= {'a': 12}
print(dict['a'], 'b' not in dict)
print(arr)
arr = [{'a': 2}, {'b': 3, 'a': 4}]
print(arr.pop())
print([x['a'] for x in arr])
# arr[0], arr[1] = arr[1], arr[0]
print(arr)
print([1,2]+[3,4])
# for i in range(2, 10):
#     print(i)

cc = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
# print(cc[1])
