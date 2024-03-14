# What is a File? 
- File is a named location on disk to store information.
They are used to store data parmanently.
Data is stored in non-volatile memory.
We can retrive data whenever required.

## Types of files:-
1) Text files:
   - Stores data in the form of characters. It is used to store data and strings. Ex: text files
2) Binary files:
   - Stores data in the form of bytes (group of 8 bits). Ex: Audio file, video file, Image file,  pdf file

## What is file Handling
 * File handling means :-
   - Opening a file,
   - Performing some operations on it,
   - Closing a file.

## Opening a file :
 - Python provides an in-built function open() to open a file.
 - Syntax :
      ```
         f = open(filename, mode='r', buffering, encoding=None, errors=None, newline=None, closefd=True) 
   ```
      - Important arguments are filename, mode  so the new Synatx will be : 
      ```
         f = open(filename, mode='r' )
      ```
 - 'filename' :- file to be accessed.
 - 'mode' :- access mode(purpose of opening a file).
 - ' f ' :- file handler, file pointer.
 - buffering :- 
   - Positive Integer value used to set buffer size for file.
   - In text mode, buffer size should be 1 or more than 1.
   - In binary mode, buffer size can be 0.
   - Default size = 4096 - 8192 bytes.
 - encoding :-
   - Encoding type used to decode and encode file.
   - Should be used in text mode only.
   - Default value depends on OS.
   - For Windows :- cp1252
 - errors :-
   - Represents how encoding and decoding errors are to be handled.
   - Cannot be used in bibary mode.
   - Some standard values are : strict, ignore replace etc.
 - newline :-
   - It can be \n, \r, \r\n.
   - Default value depends on file.

## Closing a file :-
- After performing operations, we have to close a file.
- close() :- function used to close a file.
- Syntax :-<br>
   <code>file_handler.close()</code>

###  What happens when we close a file?
- File object is deleted from memory and file is no more accessable unless we open it again.

###  What happens when we don't close a file?
 - After program execution, python garbage collector will destroy file object and close file automatically.
 - Note: Don't rely on Garbage Collector.

## File object variables:
- name :- has name of specific file.
- mode :- mode of specific file.
- closed :- has boolean value. Shows file closed or not.
- encoding :- has encoding name.
- Syntax :-<br>
  <code> File_object.variable_name </code>

## File object methods :
1) readable()
2) writable()

readable():- 
- This method is used to check whether file is readable or not.
- True :- if file is readable
- False :- if file is not readable.

writable():- 
- This method is used to check whether file is writeable or not.
- True :- if file is writeable
- False :- if file is not writeable.
      
### Check file exists or not?
isfile():-
- This method is used to check file exists or not.
- This method belongs to path module which is sub-module of os module.
- Syntax:- 
```
import os 
os.path.isfile("filename")
```

## Ways of closing files :
1) Normal way
2) Using exception handling
3) with statement

*Normal Way:- 
```
f= open('filename', mode='r') 
   #operations   //Exception stops normal flow of program 
f.close()
 ```

*Using exception handling:- 
```
try: 
   f= open('filename', mode='r') 
finally: 
   f.close()
```

*With statement:- <br>
```
with open('filename', mode='r') as f: 
   #operations
```

- Example:- 
```
with open("hello.txt", "r") as f:
   data = f.read()
   print(data)
```
## Mode of opening file :-
- when we open a file for operations, we have to specify mode. Mode specifies the purpose of opening file. There are 2 types of modes:-
   1) Text mode
   2) Binary mode

- Text mode :
   - When we open a file in text mode, python treats it's content as "str" type.
   - When we get data from a text mode file, python first decodes the raw bytes using either a platform dependent encoding or specifeied encoding.

- Binary mode : 
   - When we open a file in binary mode, python uses the data without any encoding. Binary mode file reflects the raw data directly in the file.
   - Python treats file contents as "byte" type. These modes are used while dealing with non-text files like images, audios, videos etc.

Text modes : 
```
Read Only (‘r’)
Read and Write (‘r+’)
Write Only (‘w’)
Write and Read (‘w+’)
Append Only (‘a’)
Append and Read (‘a+’)
Create a new file an write data into it (‘x’), if file already exists it will give an error.
```

Binary modes:
```
Read Only (‘rb’)
Read and Write (‘rb+’)
Write Only (‘wb’)
Write and Read (‘wb+’)
Append Only (‘ab’)
Append and Read (‘ab+’)
Create a new file an write data into it (‘xb’), if file already exists it will give an error.
```

## Reading data from files :
To read content of file, we have following three methods:
1. read()
2. readline()
3. readlines()

read() :-
- This method is used to read data/content from a file and returns it as a string on text mode. It returns bytes in binary mode.
- Syntax : <br>
<code> file_object.read(size)</code> 'size' argument is optional. <br>
<u>size</u> :- it represents the number of characters to be read in text mode.

readline() :-
 - This function is used to read a single line from a file.
 - Syntax : <br>
 <code>file_object.readline(size)</code>

readlines() :-
 - This method is used to read all lines from a file and returns a list of lines.
 - Syntax : <br>
 <code>file_object.readlines()</code>

### Reading File Using For Loop :
```
with open('hello.txt', mode='r') as f:
    for line in f:
        print(line, end='')
```

## tell() method :-
 - This method is used to find the current position of a file pointer from the beginning of the file.
  - Position starts from 0. It is just like indexing in string.
 - Syntax : <br>
 <code>file_object.tell()</code>

## seek() method :-
 - This method is used to change the position of file pointer.
  - Remember, file pointer position is always counted from the beginning.
  - Syntax :- <br>
  <code>file_object.seek(position)</code>


### Q : Find Number of characters,words and lines in File : 
```
with open('hello.txt', mode='r') as f:
    number_of_lines = 0
    number_of_chars = 0
    number_of_words = 0
    
    for line in f:
        number_of_lines += 1
        line = line.strip('\n')
        number_of_chars += len(line)
        list1 = line.split()
        number_of_words += len(list1)
    print(f'number_of_lines = {number_of_lines}')
    print(f'number_of_chars = {number_of_chars}')
    print(f'number_of_words = {number_of_words}')
```

## Writing in a file :-
 - In order to write data in a file, we have to open in a mode which provide the facility of writing data ex. w, a, x etc.

'W' mode :
 - It opens the file to write only.
 - It overwrites the data in a file.
 - If a file doesn't exist, it creates a new file and write into it.
 - The file pointer exists at the beginning of file.
 - Mainly 2 methds are used for writing data in files :
   1. write()
   2. writelines()
 - Syntax : <br>
 <code>file_object.write('data in string form')</code>

## Copy Content Of One File Into Another File :
- using write() method :
```
with open('test1.txt', mode='r', encoding='utf-8') as f1:
    with open('test2.txt', mode='w') as f2:
        data = f1.readlines()
        for line in data:
            f2.write(line)
```       

- using writelines() method :
    - This method is used to write a group of lines of strings into the file represented by a file object.
     - Group of strings are stored in list, tuple or set.
   - Syntax : <br>
   <code>file_object.writelines(list/tuple/set)</code>
   - Example :
```
with open('test2.txt', mode='w') as f:
    lines_list = ['You ','are ','watching ','this']
    f.writelines(lines_list)
```


## x mode in Python : 
 - Used to write data in a file.
 - Note : It writes only in a new line.
 - It is avoids data lossas it creates a new file.
 - Example :
 ```
 data = "This is used to test the x-mode in Python."
 with open('xmode.txt', mode='x') as f:
    f.write(data)
```

## Merging Multiple Text Files :
```

import os
files = []
merged_data = ''

while True:
    f_name = input("Enter the file name : ")
    files.append(f_name)
    ans = input("Want to add another file? (y/n)").lower()
    if ans != 'y':
        break

for file in files:
    filename = file+'.txt'
    # to check whether the file is present or not
    if os.path.isfile(filename):
        with open(filename, mode='r') as f:
            merged_data = merged_data + f.read() + '\n'
print(merged_data)

with open(input('Enter final file name : ') + '.txt', mode='x') as f1:
    f1.write(merged_data)
    print("Merging is done, Thanks and check the file")
```

## Renaming multiple files :
```
import os
path = input('Enter the path : ')    #D:\Study\Python\File-Handling-In-Python\Cars\
path = path.replace('\\', '/')
print(path)

# rename(old_name, new_name)
file_list = os.listdir(path)  # it creates list of all file names
print(file_list)

def main():
    i = 1
    for filename in os.listdir(path):
        old_name = path + filename
        new_name = path + 'car-' + str(i) +'.jpg'
        os.rename(old_name, new_name)
        i += 1
    print(f"Renaming done successfully!!!" )
        
main()
```

##  r+ and w+ Mode in File Handling :
r+ mode :
   - It means Read & Write mode.
   - the file pointer position at the beginning of the file.
   - the r+ throws an error if file doesn't exixt.
   - opens an exixting file without truncating it.
   - Use :-
      - If you want to read data first and write (append) data to same file.

w+ mode :
   - It means Write & Read mode.
   - the file pointer position at the beginning of the file.
   - the w+ creates a new file if file doesn't exixt.
   - opens an exixting file and truncating it first.
   - Use :-
      - When you want to write data and read the same data after writing.


Examples:
- using r+ mode :
```
with open('data.txt', mode='r+') as f:
    data = f.read()
    print(data)
    f.write("This is new text adding for r+ mode")
```

- using w+ mode :
```
with open('data.txt', mode='w+') as f:
     f.write("This is new text adding for w+ mode")
     f.seek(0)
     data = f.read()
     print(data)
```