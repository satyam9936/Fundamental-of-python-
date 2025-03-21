#print("hello world")

#complex number
z=4+5j
print(z)
print(type(z))


print(abs(-4))

#learning a list

students=["Mohan", "Satyam", "Ansh"]

print(students)
print(type(students))

list2= list(students)
print(list2)

list3=list("Satyam")
print (list3)

list4= list((3,4,"Satyam"))
print(list4)


#Accesssing the element of list
L1= [1,2,23,4,5]
print(L1)

print(L1[-5])
#inserting the Array in the list
arr=[1,2,3,4,5,6]
arr.append(8)
print(arr)

arr.insert(1,43)
print(arr)
#insering or extend Two array
L1=[1,2]
L2=["satyam, Ansh"]

L1.extend(L2)
print(L1)

#Remove the element from the list

arr=[2,3,4,5,6]
arr.remove(3)

print(arr)

arr=[2,3,4,4,5]
arr.remove(4)
arr.remove(4)

print(arr)
#pop the last element
print(arr.pop(2))
print(arr)

students=['a','b','c']

students[2]='f'
print(students)

students[1:4]='m','n','o'
print(students)




