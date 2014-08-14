import os
import random

files = os.listdir('/Users/eshagdar/Desktop/files')
index = random.randrange(0,len(files))
print files[index]