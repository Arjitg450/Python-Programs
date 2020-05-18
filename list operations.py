#list operations
l1=[1,2,3,4]
#1-lst.append,o/p-[1, 2, 3, 4, [5, 6, 7, 8]]
l2=[5,6,7,8]
l1.append(l2)
print(l1)

#2-lst.extend,o/p-[1, 2, 3, 4, 5, 6, 7, 8]

l1=[1,2,3,4]
l2=[5,6,7,8]
l1.extend(l2)
print(l1)

#3-lst.insert,o/p-[1, 1.5, 2, 3, 4]

l1=[1,2,3,4]
l2=[5,6,7,8]
l1.insert(1,1.5)
print(l1)

#4-lst.remove,o/p-[1, 3, 4]  (to remove item based on value)

l1=[1,2,3,4]
l2=[5,6,7,8]
l1.remove(2)
print(l1)

#5-delete (to remove item based on index value)
#o/p_1 - [2, 3, 4]
'''o/p_2 - Traceback (most recent call last):
  File "H:/python programs/list operations.py", line 36, in <module>
    print(l1)
NameError: name 'l1' is not defined'''

l1=[1,2,3,4]
l2=[5,6,7,8]
del l1[0]
print(l1)
#del l1
#print(l1)

#6-lst.pop,o/p-[1, 2, 4] (to pop item based on index value)

l1=[1,2,3,4]
l2=[5,6,7,8]
l1.pop(2)
print(l1)

#7-lst.reverse

#reverse is reverses the entire list,o/p-['four', 'three', 'two', 'one']
lst = ['one', 'two', 'three', 'four']
lst.reverse()
print(lst)


#8- sorted(lst)
#create a list with numbers
numbers = [3, 1, 6, 2, 8]
sorted_lst = sorted(numbers)
print("Sorted list :", sorted_lst)
#original list remain unchanged
print("Original list: ", numbers)



lst = [1, 20, 5, 5, 4.2]
#sort the list and stored in itself
lst.sort()
# add element 'a' to the list to show an error
print("Sorted list: ", lst)

#9- lst.split,o/p-['one', 'two', 'three', 'four', 'five']
#let's take a string
s = "one,two,three,four,five"
slst = s.split(',')
print(slst)

#o/p - ['This', 'is', 'applied', 'AI', 'Course']
s = "This is applied AI Course"
split_lst = s.split() # default split is white-character: space or tab
print(split_lst)


#10- list slicing

numbers = [10, 20, 30, 40, 50,60,70,80]
#print alternate elements in a list
print(numbers[::2])#it means 0 se lekar last tak ,1 ko chod kar agla print kro ,just like range

#10- lst.count ,count for a frequency of a particular number in list
#o/p-1 becasuse 32 comes  only 1 time in list 

lst=[1,32,344]
a=lst.count(32)
print(a)

#list comprehensions

























