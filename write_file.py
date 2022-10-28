f = open("pelican.txt", "a")
f.write("A wonderful bird is the pelican\n")
f.write("His bill holds more than his belican\n")
lines = ["He can take in his beak,\n", "Enough food for a week,\n","But I'm damned if I see how the helican.\n"]
f.writelines(lines)
f.close()
print(f)