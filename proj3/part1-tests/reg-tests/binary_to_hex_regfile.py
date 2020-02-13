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
		r1 = ''.join(hexes[:2])		# Op#
		r2 = ''.join(hexes[2:10])	# ra
		r3 = ''.join(hexes[10:18])	# sp
		r4 = ''.join(hexes[18:26])	# t0
		r5 = ''.join(hexes[26:34])	# t1
		r6 = ''.join(hexes[34:42])	# t2
		r7 = ''.join(hexes[42:50])	# s0
		r8 = ''.join(hexes[50:58])	# s1
		r9 = ''.join(hexes[58:66])	# a0
		r10 = ''.join(hexes[66:74])	# ReadData1
		r11 = ''.join(hexes[74:82])	# ReadData2
		r12 = ''.join(hexes[82:84])	# rs1
		r13 = ''.join(hexes[84:86])	# rs2
		r14 = ''.join(hexes[86:88])	# rd
		r15 = ''.join(hexes[88:89])	# RegWEn
		r16 = ''.join(hexes[89:97])	# WriteData
		result = [r1,r14,r12,r13,r15,r16,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11]
		results.append(result)
	print ("Op#\trd\trs1\trs2\tRegWEn\tWriteData\tra (x1)\t\tsp (x2)\t\tt0 (x5)\t\tt1 (x6)\t\tt2 (x7)\t\ts0 (x8)\t\ts1 (x9)\t\ta0 (x10)\tReadData1\tReadData2")
	for r in results:
		string = '\t'.join(r)
		print (string)

if __name__ == "__main__":
	main(sys.argv)
