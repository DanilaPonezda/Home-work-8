
fh = open("logs.txt", "w+" )



fh.write(input("?: ") + "\n\n\n\n\nDanylo Ponezhda")



fh.close()

fh = open("logs.txt", "r")

g= fh.read()
print(g)


fh.close()