#!/usr/bin/python3

if __name__ == "__main__":
	import sys

	count = len(sys.argv) - 1
	result = 0
	for c in range(count):
		result = result + int((sys.argv[c +1 ]))
	print(result)
