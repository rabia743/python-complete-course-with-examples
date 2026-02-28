with open("file.txt")as f:
    content = f.read()

with open("file_copy.txt","w")as f:
    f.write(content)