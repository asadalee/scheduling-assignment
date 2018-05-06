q1_process= []
q2_process= []
q3_process= []
q1=-1
q2=-1
q3=-1
n= int (raw_input ("enter total number of processes: "))
time1= int (raw_input ("enter time slice of queue 1: "))
time2= int (raw_input ("enter time slice of queue 2: "))
for i in range(n):
	print "enter information for ", i+1,"th process"
	q1+=1
	q1_process.append([])
	q1_process[i].append(raw_input ("enter process name: ") )
	q1_process[i].append (int(raw_input ("enter process arrival time: ")))
	q1_process[i].append (int (raw_input ("enter process burst time: ")))
	print ''
q1_process.sort(key= lambda q1_process: q1_process[1])
burst= []
for i in range(n):
	burst.append([])
	burst[i]= q1_process[i][2]
final= q1_process[0][1]
i=-1
next_index= "true"
total_waiting= 0
total_turnaround= 0
k=-1
#total_processes= n
#while total_processes>0:
for j in range(n):

	if next_index== "true":
		i+=1
	#if i>=total_processes:
	#	i=0
	next_index= "true"
	if burst[i] <= time1:
		final+=burst[i]
		burst[i]=0
		waiting= final-q1_process[0][1]-q1_process[0][2]
		turnaround= final-q1_process[0][1]
		total_waiting+= waiting
		total_turnaround+= turnaround
		print "process ",q1_process[0][0]," arrive at ",q1_process[0][1]," & terminate at ",final
		print "waiting time of this process is ",waiting
		print "turnaround time of this process is ",turnaround
		print ''
	else:
		final+=time1
		burst[i]-=time1
	if burst[i]==0:
		burst.remove(burst[i])
		#total_processes-=1
		next_index= "false"
	else:
		k+=1
		q2_process.append([])
		q2_process[k].append(q1_process[0][0])
		q2_process[k].append(q1_process[0][1])
		q2_process[k].append(q1_process[0][2])
	q1_process.remove(q1_process[0])

next_index= "true"
i=-1
l=-1
if k>=0:
	for j in range(k+1):
		if next_index== "true":
			i+=1
		#if i>=total_processes:
		#	i=0
		next_index= "true"
		if burst[i] <= time2:
			final+=burst[i]
			burst[i]=0
			waiting= final-q2_process[0][1]-q2_process[0][2]
			turnaround= final-q2_process[0][1]
			total_waiting+= waiting
			total_turnaround+= turnaround
			print "process ",q2_process[0][0]," arrive at ",q2_process[0][1]," & terminate at ",final
			print "waiting time of this process is ",waiting
			print "turnaround time of this process is ",turnaround
			print ''
		else:
			final+=time2
			burst[i]-=time2
		if burst[i]==0:
			burst.remove(burst[i])
			next_index= "false"
		else:
			l+=1
			q3_process.append([])
			q3_process[l].append(q2_process[0][0])
			q3_process[l].append(q2_process[0][1])
			q3_process[l].append(q2_process[0][2])
		q2_process.remove(q2_process[0])

if l>=0:
	start= final
	finish= final+burst[0]
	for i in range(l+1):
		waiting = finish-q3_process[i][1]-q3_process[i][2]
		turnaround = finish- q3_process[i][1]
		total_waiting+= waiting
		total_turnaround+= turnaround
		print "process ",q3_process[i][0]," arrive at ",q3_process[i][1]," & terminate at ",finish
		print "waiting time of this process is ",waiting
		print "turnaround time of this process is ",turnaround
		print ''	
		start= finish
		if i<l :
			finish+= burst[i+1]
print "average waiting time is ",total_waiting/n
print "average turnaround time is ",total_turnaround/n
