with open("log.txt")as f:
    content = f.read()

if("python" in content):
    print("yes this python in content")

else:
    print("no this python in content")
    