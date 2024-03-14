## Only in read mode:
# f = open("hello.txt")
# if f:
#     print('File successfully opened.')


## Only in write mode:
# f = open("hello.txt", mode='w')
# if f:
#     print('File successfully opened.')
# print(type(f))


# f = open('hello.txt', mode='r', buffering=10, encoding='utf-8')
# if f:
#     print("Opended")
# print(f)


# # Close a file
# f = open('hello.txt')
# # perform operations like read, write, append etc
# f.close()

# # Accessing object variables
# f = open('hello.txt', mode='r', encoding='utf-8')
# print("file name is", f.name)
# print("Encoding is", f.encoding)
# print("Mode is", f.mode)
# print("Is file closed", f.closed)
# f.close()
# print("Is file closed", f.closed)

# # File Object methods
# # f = open('hello.txt', 'r')
# # f = open('hello.txt', 'w')
# f = open('hello.txt', 'w+')
# print(f.readable())
# print(f.writable())
# f.close()

# # Check file exists or not?
# import os
# print(os.path.isfile('hello.txt'))
# print(os.path.isfile('file.txt'))


# # opening file in text mode
# f = open('hello.txt', 'r')
# data1 = f.read()
# print("File in Text mode : ", data1)
    
# # opening file in binary mode
# with open('hello.txt', mode='rb') as f:
#     data2 = f.read()
#     print("File in binary mode : ", data2)

# # Reading data from files :
# # using read()
# with open('hello.txt', mode='r') as f:
#     data = f.read(3)
#     data1 = f.read(7)
#     print(data, data1)

# # using readline()
# with open('hello.txt', mode='r') as f:
#     data = f.readline()
#     data1 = f.readline()
#     print(data, end='')
#     print(data1)

# # using readlines()
# with open('hello.txt', mode='r') as f:
#     data = f.readlines()
#     print(data)


# # Reading File Using For Loop :
# with open('hello.txt', mode='r') as f:
#     for line in f:
#         print(line, end='')


# # tell() method:
# with open('hello.txt', mode='r') as f:
#     print(f.tell())
#     f.read(10)
#     print(f.tell())
#     f.read()
#     print(f.tell())

# # seek() method :-
# with open('hello.txt', mode='r') as f:
#     print(f.tell())
#     print(f.read(10))
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     print(f.read())
    
    
# # Find Number of characters,words and lines in File :
# with open('hello.txt', mode='r') as f:
#     number_of_words = 0
#     number_of_chars = 0
#     number_of_lines = 0
    
#     for line in f:
#         number_of_lines += 1
#         line = line.strip('\n')
#         number_of_chars += len(line)
#         list1 = line.split()
#         number_of_words += len(list1)
#     print(f'number_of_lines = {number_of_lines}')
#     print(f'number_of_chars = {number_of_chars}')
#     print(f'number_of_words = {number_of_words}')

# # Writing in a file :-
# with open('data.txt', mode='w') as f:
#     # f.write("This for write method test. \nThank you\n")
#     # f.write("This is another test.")
#     n = f.write("This is overwriting the previous data.")
#     print(n)

# # Copy Content Of One File Into Another File:
# # using write() method :
# with open('test1.txt', mode='r', encoding='utf-8') as f1:
#     with open('test2.txt', mode='w') as f2:
#         data = f1.readlines()
#         for line in data:
#             f2.write(line)
        
# # using writelines() method :
# with open('test2.txt', mode='w') as f:
#     lines_list = ['You ','are ','watching ','this']
#     f.writelines(lines_list)

# # x mode in Python:
# data = "This is used to test the x-mode in Python."
# with open('xmode.txt', mode='x') as f:
#     f.write(data)


# # Merging Multiple Text Files :
# import os
# files = []
# merged_data = ''

# while True:
#     f_name = input("Enter the file name : ")
#     files.append(f_name)
#     ans = input("Want to add another file? (y/n)").lower()
#     if ans != 'y':
#         break

# for file in files:
#     filename = file+'.txt'
#     # to check whether the file is present or not
#     if os.path.isfile(filename):
#         with open(filename, mode='r') as f:
#             merged_data = merged_data + f.read() + '\n'
# print(merged_data)

# with open(input('Enter final file name : ') + '.txt', mode='x') as f1:
#     f1.write(merged_data)
#     print("Merging is done, Thanks and check the file")

# # Renaming multiple files :
# import os
# path = input('Enter the path : ')    #D:\Study\Python\File-Handling-In-Python\Cars
# path = path.replace('\\', '/')
# print(path)

# # rename(old_name, new_name)
# file_list = os.listdir(path)  # it converts the files into list
# print(file_list)

# def main():
#     i = 1
#     for filename in os.listdir(path):
#         old_name = path + filename
#         new_name = path + 'car-' + str(i) +'.jpg'
#         os.rename(old_name, new_name)
#         i += 1
#     print(f"Renaming done successfully!!!" )
        
# main()

# r+ and w+ Mode in File Handling :
# using r+ mode:
# with open('data.txt', mode='r+') as f:
#     data = f.read()
#     print(data)
#     f.write("This is new text adding for r+ mode")

# # using w+ mode:
# with open('data.txt', mode='w+') as f:
#     f.write("This is new text adding for w+ mode")
#     f.seek(0)
#     data = f.read()
#     print(data)