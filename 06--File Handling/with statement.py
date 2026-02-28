# with staement its replace f.close()

with open("my second file","w") as f:
    f.write("hello i am a beginner python developer")


with open("my second file",) as f:
    data = f.read()
    print(data)

# jub hum with stateme likta ha tu f.close function likna ki need nahi ha