dict={"ariya":20,"anu":8,"diya":67}
for key in list(dict):
    if key=="anu":
        del dict[key]

print(dict)

