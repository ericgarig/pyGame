# 2014-08-20 ( eshagdar )
# randomly pick a file from a specified dir, and execute it.

import os
import random

my_dir = os.path.dirname(os.path.realpath(__file__))
files = os.listdir(my_dir + '/Maps')
index = random.randrange(0,len(files))
the_file = 'maps/' + files[index]
subLocals = dict()
execfile(the_file, dict(), subLocals)

print the_file, subLocals['script_result']
