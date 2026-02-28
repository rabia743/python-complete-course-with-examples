with open("file.txt")as f:
    content1 = f.read()

# hum ab iska name ko renamed ker de ga
with open("renamed_by_python.txt","w")as f:
    f.write(content1)