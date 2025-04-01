#customize the errors
try:
    #open a file and read the file contents
    a_file = open('sample.txt','r')
    reading1 = a_file.readline()
    reading2 = a_file.readline()
    print("line 1: ",reading1)
    print("line 2: ",reading2)
    a_file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")