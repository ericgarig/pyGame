import os, random

files = os.listdir('/Users/ericgarig/pyGame/Maps')
index = random.randrange(1,len(files))   # do not include the .DS_Store file
#print files[index]

with open("Maps/"+files[index]) as file:	# Use file to refer to the file object
    data = file.read()
    exec( data )


print MapClass.allSprites