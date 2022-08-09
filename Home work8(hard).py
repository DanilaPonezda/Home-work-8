fh = open("logs.txt", "r")
a = fh.read()
fh.close()

fh = open("logs(copy).txt", "w")

fh.write(a)

fh.close()


