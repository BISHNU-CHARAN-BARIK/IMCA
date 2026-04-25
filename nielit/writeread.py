with open("writeread.txt","w+") as f:
    f.write("This is 3rd line.\n")
    f.seek(2,0)#it move the object pointer to first position..and only 0 is whence for the text data
    data=f.read()
    print(data)
    f.seek(0,0)
    data=f.read()
    print(data)

   