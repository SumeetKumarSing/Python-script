file = open("sample.txt","w")  # Create file and write on it

file.write("Hello From sumeet")

file.close()

#---------------------

file = open("sample.txt","r") # Read file sample.txt 
data = file.read()
print(data)
file.close()

#--------------------

file = open("sample.txt","a")  # Append  file sample.txt with text as "nWelcome to india"
file.write("\nWelcome to india")
file.close()

#-----------

file = open("sample.txt","r+") # Read file sample.txt # this will add and write
file.write("Hi")
file.seek(0)            #Curseor goes to the start poastion
print(file.read()) # Read the file after write
file.close()
