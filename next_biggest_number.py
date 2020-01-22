#!/usr/bin/python3
import sys
import itertools

def main():
	next_biggest_number(sys.argv[1])


def next_biggest_number(num):
	sortedstring=''.join(sorted(list(str(num))))
	perms = [] 
	for i in itertools.permutations(sortedstring):
		value=''.join(i)
		if value not in perms: 
			perms.append(value) 
	next=perms.index(str(num))+1
	if next == len(perms):
		return -1
	else:
		return int(perms[next])

if __name__ == "__main__":
    main()