#!/usr/bin/env python2.7

arr = "\\x00"

for i in range(1,16):
	arr = arr + "\\x0" + str(hex(i)).strip("0x")

for i in range(16,256):
	if len(str(hex(i)).strip("\\0x")) == 1:
		print "here"
		char = "\\x" + str(hex(i)).strip("\\0x") + "0"
		arr = arr + char
	else:
		arr = arr + "\\x" + hex(i).strip("\\0x")

print arr
