import os
if os.path.exists("write.txt"):
    print("file exists")
else:
    print("File does not exists")
os.rename("write.txt","write_file.txt")
if os.path.exists("write.txt"):
    print("file exists")
else:
    print("File does not exists")
