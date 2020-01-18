# Extracting specific information from a file (  Here, it is Blast output file)
file = open('blast-12.out', 'r')
x = []
for line in file:
    words = line.split()
    x = int(words[11]) # Converting 11th word to int in every line for comparision.
    if (x >=  221199) & (x <=222701):
        y =str(x)   # Converting integer back to string
        if y in line:
            print(line)
        else:
            pass
