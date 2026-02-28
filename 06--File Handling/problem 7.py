with open("log.txt") as f:
    lines = f.readlines()   # read all lines

lineno = 1
for line in lines:
    if "python" in line.lower():    # check each line
        print(f"Yes, 'python' is in line no: {lineno}")
        break
    lineno += 1
else:
    print("No, 'python' is not available")
