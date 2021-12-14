#import input file
f = open("input_1.txt")

#extract file to list and cast to int
L = [int(i) for i in f.readlines()]

#declare prev as the first list item and init counter
prev = L[0]
counter = 0

#compare list items and add to counter
for i in L[1:]:
	if i > prev:
		counter += 1
	prev = i

print(counter)