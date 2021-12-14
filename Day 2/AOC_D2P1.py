#import input file
f = open("input_2.txt")

#extract information to list
L = f.readlines()

#init horizontal and depth counters
horizontal = 0
depth = 0

#loop for all list items
for i in L:

	#split each item at white space
	x = i.split()
	
	#match commands and apply casted integer to corresponding counter
	match x[0]:
		case "forward":
			horizontal += int(x[1])
		case "up":
			depth -= int(x[1])
		case "down":
			depth += int(x[1])
			
print(horizontal*depth)
