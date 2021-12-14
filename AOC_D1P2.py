#import input file
f = open("input_1.txt")

#extract information to list and cast to int
L = [int(i) for i in f.readlines()]

#declare prev as sum of the first three list items
prev = L[0] + L[1] + L[2]

#init counter
count = 0

#compare sums and iterate counter
for i in range(1,len(L)-2):
	cmpr = L[i] + L[i+1] + L[i+2]
	if cmpr > prev:
		count += 1
	prev = cmpr

print(count)