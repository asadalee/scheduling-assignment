process= []
n= int (raw_input ("enter total number of processes: "))
time= int (raw_input ("enter time slice: ") )
print ''
for i in range(n):
	print "enter information for ", i+1,"th process"
	process.append([])
	process[i].append(raw_input ("enter process name: ") )
	process[i].append (int(raw_input ("enter process arrival time: ")))
	process[i].append (int (raw_input ("enter process burst time: ")))
	print ''
process.sort(key= lambda process: process[1])
burst= []
for i in range(n):
	burst.append([])
	burst[i]= process[i][2]
final=process[0][1]
i=-1
next_index= "true"
total_waiting= 0
total_turnaround= 0
total_processes= n
while total_processes>0:
	if next_index== "true":
		i+=1
	if i>=total_processes:
		i=0
	next_index= "true"
	if burst[i] <= time:
		final+=burst[i]
		burst[i]=0
		waiting= final-process[i][1]-process[i][2]
		turnaround= final-process[i][1]
		total_waiting+= waiting
		total_turnaround+= turnaround
		print "process ",process[i][0]," arrive at ",process[i][1]," & terminate at ",final
		print "waiting time of this process is ",waiting
		print "turnaround time of this process is ",turnaround
		print ''
	else:
		final+=time
		burst[i]-=time
	if burst[i]==0:
		burst.remove(burst[i])
		process.remove(process[i])
		total_processes-=1
		next_index= "false"

	if total_processes==0 :
		average_waiting= total_waiting/n
		average_turnaround= total_turnaround/n
		print "average waiting time is ",average_waiting
		print "average turnaround time is ",average_turnaround
		print ''
