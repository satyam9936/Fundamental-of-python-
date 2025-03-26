#open the file in the read mode 
#file =open("Filehandling/file.txt","r")


#using file i can read 
#through loop

'''for line in file :
    print(line)'''
 #using the statement
with open("Filehandling/file.txt", 'r') as file:
    data=file.read()
    print(data)
#read only the first number of character
#modes

#code for writing the file 

'''file=open("Filehandling/file2.txt",'w')
file.write("hello world") 
file.write("first numbers") 
file.close()      '''

#code for appending /writing with 
'''with open('Filehandling/file3.txt','w') as file:
    file.write("hello everyone ")'''
    
'''import os

os.path.isfile("Filehandling/file2.txt")'''