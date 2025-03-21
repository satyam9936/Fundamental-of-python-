#Polymorphism or #Duck typing concept

class BirdFly:
  def flybird(self,bird):
    bird.fly()

class Parrot:
  def fly(self):
    print("Parrot can fly")

class Ostrich:
  def fly(self):
    print("Ostrich can not fly")
p=Parrot()
O=Ostrich()
pf=BirdFly()
pf.flybird(p)
pf.flybird(O)

#Relationship of Assoication
'''hasA test
has A country
compostion
Human body  Heart
depends -Composition Relationship 

'''
#aggregation
class Car:
  def __init_(self,brand,color):
    self.brand=brand
    self.color=color
class Person:
  def __init(self,name,car):
    self.name=name
    self.car=car


#compostion
class Engine:
  def start(self):
    print("Engine started")
class Car:
  def __init__(self):
    self.engine=Engine()
  def drive(self):
    self.engine.start()
car=Car()
car.drive()



#exception handling
'''error- event stops eg- power failure, os crash
exception- unaccepted behaviour 
in python error and exception is same 
'''
'''str="Satyam"
for s in str:
  print(s)'''
#exception 
def cube_root(num):
  #check number is pos and if not raise exception
  assert(num >=0),  "pass me a positive number"
  return num**(1/3)

print(cube_root(8))

try:
  val=cube_root(-8)
  print(val)
except:
  print("please provide me a positive number for cube root")

print("last line")



#try,except,finally,else

def operate(num):
  try:
    result=5/num
  except ZeroDivisionError:
    print("cant divide a number by 0")
  finally:
    print("this portion is excuted ")
operate(0)


#inheritance
#Run time Error
class EmptyException(RuntimeError):
  def __init__(self, *args):
    self.args=args
var=""

try:
  raise EmptyException("this variable is an empty string")
except EmptyException as e:
  print(e.args)