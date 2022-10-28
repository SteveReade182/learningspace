# f = open("pelican.txt", "r").

# with open("pelican.txt") as pelican: f = pelican.read()
with open("pelican.txt","r") as f:
    contents = f.readlines()
    print(type(contents))
    print(len(contents))

    for line in contents:
        newline = line.strip("\n")
        newline = newline.strip(",")
        print(newline)
        pass

