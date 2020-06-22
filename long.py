#! /usr/bin/python
import sys

def main():
	s=raw_input("Enter the String")
#	s = "azcbobobegghakl"
	longest = s[0]
	cu = s[0]
	for c in s[1:]:
		if c >= cu[-1]:
			cu += c
			if len(cu) > len(longest):
				longest = cu
		else:
			cu = c
	print "Longest substring in alphabetical order is:", longest

if __name__=='__main__':
	main()