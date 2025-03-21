from os import name
'''str=input("Please provide the string")
count=0
for ch in str:
    if ch.lower() in ['a','e','i','o','u']:
        count +=1
print("Total count of vowel is",count)


#faconacci series
n= int(input ("Please enter the value of n- upto which we want the fibonacci series"))
if(n<=0):
  print("Number is correct . it should be>0.entered num",n)
Problems  in For loops.ipynb
Problems  in For loops.ipynb_

[16]
0s

print(1,end=",")
if(n==1):
  pass
else:
  print(1,end=",")
  if(n==2):
    pass
  else:
    #print the remaining part of the series
    prev=1
    prev_prev=1
    for num in range(3,n+1):
     print(prev+prev_prev,end=",")
     prev,prev_prev=prev+prev_prev,prev'''

     #the prime numberis prime or not
'''num=int(input("Please enter the number"))
isPrime=True
if(num<=1):
  isPrime=False
for i in range(2,int(num/2)+1):
  if(num%i==0):
    isPrime=False
    break
print("The number is prime",isPrime)'''
#print the multiplication of number
'''num=int(input("enter the multiplication of number"))
for i in range(1,11):
  print(num, "*",i,"=",num*i)'''
'''for i in range(4):
  for j in range (i+1):
    print("*",end="")'''


class Person:
  def __init__(self,name,age):
     self.name=name
     self.age=age
  def __init__(self, name):
     self.name=name
per=Person("satyam")
print(per.name)


class Person:
  def __init__(self,name,age=99,hobby="cricket"):
    self.name=name
    self.age=age
    self.hobby=hobby
per1= Person("satyam")
per2=Person("satyam",99)
per3=Person("satyam",99,"cricket")
print(per1.name,per1.age,per1.hobby)

#difference in instance and class
class Person:
  country="india"
  def __init__(self, name,age):
    self.name=name
    self.age=age
per1=Person("satyam",99)
per2=Person("satya",54)

print(per1.name,per1.country)
print(per2.name,per2.country)

'''method
instance
class
static method'''

#method overloading
#explict overloading
'''class Calculator :
  def add(self,a,b):
    return a+b
  def add(self,a,b,c):
    return a+b+c
cal=Calculator()
print(cal.add(10,20))'''
#implict overloading
class Calculator :
  def add(self,a,b,c):
    return a+b+c
  def add(self,a,b,c):
    return a+b+c
cal=Calculator()
print(cal.add(10,20,30))
print(cal.add(10,20,40))

#Access Modifier
'''1-public and 2-private'''
#encapsulation
'''bundling of data into single unit
stae , and behaviour of method
hide from private
1-All the field should be private
2-Getter and setter public method to allow the controller
'''
'''def getName(self):
  return self.__name
def setName(self,name):
  self.__name=name
  def getCar(self):
    return self.__car
def setCar(self,car):
  self.__car=car'''

#types of  inheritance 
class Animal:
  def __init__(self,name,age):
    self.name=name
    
  def eat(self):
    print ("animal is eating")
class Dog(Animal):
  def __init__(self,name,age,color):
    super().__init__(name,age)
    self.color=color
#Hybrid Inheritance