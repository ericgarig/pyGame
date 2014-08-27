import sys

sys.path.insert(0, '../')

from mapClass import *


def main():
	print '----starting Level01'
	floor04 = MapClass(10,500,400,90)
	print '---', floor04.rect
	return floor04


script_result = main()