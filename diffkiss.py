#!/usr/bin/python3

import sys

inFile1 = open(sys.argv[1], "r")
inFile2 = open(sys.argv[2], "r")

masterLines = list()
subsetLines = list()
missingLines = list()

for aLine in inFile1:
	if (len(aLine) > 0):
		masterLines.append(aLine.strip())
print("Master has %d lines" % len(masterLines))

for aLine in inFile2:
	if (len(aLine) > 0):
		subsetLines.append(aLine.strip())
print("Subset has %d lines" % len(subsetLines))

inFile1.close()
inFile2.close()

for aLine in masterLines:
	if ((subsetLines.count(aLine) == 0) and (len(aLine) > 0)):
		missingLines.append(aLine)
print("Done %d missing lines detected" % len(missingLines))

print("List of missing lines:")
for aLine in missingLines:
	print(aLine)
