#! /usr/bin/env python3

from __future__ import print_function
import sys
def main(args):
	file = open(args[1])
	lines = [l for l in file.readlines()]
	def mapper(strr):
		try: 
			return hex(int(strr, 2))[2:]
		except Exception:
			return 'x'
	results = []
	for l in lines:
		hexes = list(map(mapper,l.split()))
		r1 = ''.join(hexes[:2])
		r2 = ''.join(hexes[2:10])
		r3 = ''.join(hexes[10:11])
		r4 = ''.join(hexes[11:19])
		r5 = ''.join(hexes[19:27])
		result = [r1,r3,r4,r5,r2]
		results.append(result)
	print ("Op#\tALUSel\tInputA\t\tInputB\t\tALU_Output")
	for r in results:
		string = '\t'.join(r)
		print (string)


if __name__ == "__main__":
	main(sys.argv)
