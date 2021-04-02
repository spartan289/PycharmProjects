#working with temporary files
import os
import tempfile

#get information about the temp data environment
print('gettempdir: ',tempfile.gettempdir())
print('gettempprefix:',tempfile.gettempprefix())

#create a temporary file using mkstemp

# (tempfh,tempfp)=tempfile.mkstemp(".temp","test Temp",None,True)
# f=os.fdopen(tempfh,"w+t")
# f.write("this is some temp data")
# f.seek(0)
# print(f.read())
# f.close()
# os.remove(tempfp)
#create a temp file using the temporary class
# with tempfile.TemporaryFile(mode="w+t")as tfp:
#     tfp.write("this is some temp data")
#     tfp.seek(0)
#     print(tfp.read())



#crete a temporary directory using a temporary directory class
with tempfile.TemporaryDirectory()as tdp:
    path=os.path.join(tdp,"tempfile.txt")
    tfp=open(path,"w+t")
    tfp.write("this is some temp data")
    tfp.seek(0)
    print(tfp.read())