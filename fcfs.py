process= []
n= int (raw_input ("enter total number of processes: "))
for i in range(n):
	print "enter information for ", i+1,"th process"
	process.append([])
	process[i].append(raw_input ("enter process name: ") )
	process[i].append (int(raw_input ("enter process arrival time: ")))
	process[i].append (int (raw_input ("enter process burst time: ")))
	print ''
process.sort(key= lambda process: process[1])

print "process name\tburst time\tarrival time\twaiting time\tturnaround time"
start= process[0][1]
finish= process[0][2]+ process[0][1]
total_waiting=0
total_turnaround=0
for i in range(n):
	waiting = start-  process[i][1]
	turnaround = finish- process[i][1]
	total_waiting+= waiting
	total_turnaround+= turnaround
	print process[i][0],"\t\t",process[i][2],"\t\t",process[i][1],"\t\t",waiting,"\t\t",turnaround
	start= finish
	if i<n-1 :
		finish+= process[i+1][2]
print ''
print "average waiting time: ",total_waiting/n
print "average turnaround time: ", total_turnaround/n
