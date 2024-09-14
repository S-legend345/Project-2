#Read the contents of the file
file = open('Sample_File.txt', 'r')
print(file.read())
file.close()

#Print first 10 characters
file = open('Sample_File.txt', 'r')
print(file.read(10))
file.close()

#Print the first line of the file

file = open('Sample_File.txt', 'r')
print(file.readline())
file.close()

#Reading the 1st 4 lines

file = open('Sample_File.txt', 'r')
for i in range(4):
    print(file.readline())
file.close()

#Looping through the file to print each line

file = open('Sample_File.txt', 'r')
for line in file:
    print(line)
file.close()
