with open("write.txt","r+") as f:
    data=f.read()
    print(data)
    f.write("This is 3rd line.\n")
    data=f.read()
    print(data)