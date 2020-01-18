file = open('blast-12.out', 'r')
x = []
for line in file:
    words = line.split()
    x = int(words[11])
    if (x >=  221199) & (x <=222701  	 ):
        y =str(x)
        if y in line:
            print(line)
        else:
            pass
