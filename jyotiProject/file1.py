#basics file operations in python

#open a file for writing data
#"w" means write, "r"means read,"a" means apeend,"r+"means read and write
# fp=open("testfile","w")
# fp.write("this is some text")
# fp.close()
#
#
#
#
#add data to an existing file
with open("testfile","a")as fp:
    fp.write("this is data added in the file\n")
    fp.seek(0)
    data=fp.read()
    print(data)

#read a file
# with open("testfile","r") as fp:
#     data=fp.read()
#     print(data)
#
