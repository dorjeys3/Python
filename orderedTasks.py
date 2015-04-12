import sys

file = open("input.txt",'r') # read in input file

nodes,edges = file.readline().strip().split() #assign graphs values

length = int(nodes) - 1 #get input length

connections = []		# create list of connection array
for i in range(0,length):			
	x,y = file.readline().strip().split()
	connections.append([int(x),int(y)])

i = 0
x = 1 # starting Node
myMap = []
temp = []
for i in range(0, length):
	print(connections[i])
	if(connections[i][0] == x):
		print("entered")
		temp.append(connections[i][1])
	else:
		print("not entering condition")
	   


print(temp)

"""
print("")
print("number of Nodes: " + nodes)
print("number of Edges: " + edges)
print(connections)
"""
