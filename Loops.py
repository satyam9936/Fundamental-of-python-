#loops

'''fruits=["apple", "bnana", "cherry", "dates", "elderberry"]

for x in fruits:
    print(fruits)'''

'''name= "viswaMohan"
for ch in name:
    print(name)

for i in range(8):
    print(i)

for i in range (2,7):
    print(i)'''

'''for i in range(2,10,3):
    print(i)'''
'''for i in range (10,0,-1):
    print(i)
for i in range (12,0,-3):
    print(i)'''
#break statement
'''for num in range (1,13):
    if (num%4==0):
        break
    print(num)'''

'''#continue Statement
for i in range (11):
    if(i%2 !=0):
        continue
        print(i)

#nested Loops
for i in range (10):
    for j in range (6):
        print ("hello world")
#while loops
while num>0:
    print("hello world")'''
    

'''print("hello{0[0]}and {0[1]}".format(('PW','Learner')))

num2=int(input("num2=="))
print(num1/num2)'''

#1
sum =0
for num in range (1,21):
    if num%2==0:
        sum +=num
print("sum of even number are", sum)

#2
str=input("Please provide the string")
count=0
for ch in str:
    if ch.lower() in ['a','e','i','o','u']:
        count +=1
print("Total count of vowel is",count)