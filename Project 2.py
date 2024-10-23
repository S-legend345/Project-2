# #Read the contents of the file
# file = open('Sample_File.txt', 'r')
# print(file.read())
# file.close()

# #Print first 10 characters
# file = open('Sample_File.txt', 'r')
# print(file.read(10))
# file.close()

# #Print the first line of the file

# file = open('Sample_File.txt', 'r')
# print(file.readline())
# file.close()

# #Reading the 1st 4 lines

# file = open('Sample_File.txt', 'r')
# for i in range(4):
#     print(file.readline())
# file.close()

# #Looping through the file to print each line

# file = open('Sample_File.txt', 'r')
# for line in file:
#     print(line)
# file.close()

##Project - To Find the LCM of numbers

def gcd(n1,n2):
    while (n2):
        n1, n2 = n2, n1%n2
    return n1
def LCM(n1,n2):
    lcm = n1 * n2//gcd(n1,n2)
    return lcm

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another: "))
print(LCM(n1,n2))


