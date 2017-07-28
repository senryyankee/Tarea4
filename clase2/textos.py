infile=open('contacto_de_JaimeForero.txt.1')

text=infile.readlines()


name=text[0].rstrip('\n')
date=text[1].split()
place=text[2].split(',')
message=text[3].rstrip('\n')

print name
print date
print place
print message

