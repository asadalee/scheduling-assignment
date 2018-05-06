q1_process= []
q2_process= []
q3_process= []
q1=-1
q2=-1
q3=-1
n= int (raw_input ("enter total number of processes: "))
time= int (raw_input ("enter time slice in case of round robin processes: "))
for i in range(n):
	select=int(raw_input("press 1 for system process(RR), 2 for interactive process(sjf), 3 for batch process(FCFS)"))
	if select==1:
		q1+=1
		print "enter information for ", i+1,"th process"
		q1_process.append([])
		q1_process[q1].append(raw_input ("enter process name: ") )
		q1_process[q1].append (int(raw_input ("enter process arrival time: ")))
		q1_process[q1].append (int (raw_input ("enter process burst time: ")))
		print ''
	if select==2:
		q2+=1
		print "enter information for ", i+1,"th process"
		q2_process.append([])
		q2_process[q2].append(raw_input ("enter process name: ") )
		q2_process[q2].append (int (raw_input ("enter process burst time: ")))
		print ''
	if select==3:
		q3+=1
		print "enter information for ", i+1,"th process"
		q3_process.append([])
		q3_process[q3].append(raw_input ("enter process name: ") )
		q3_process[q3].append (int(raw_input ("enter process arrival time: ")))
		q3_process[q3].append (int (raw_input ("enter process burst time: ")))
		print ''
q1_process.sort(key= lambda q1_process: q1_process[1])
q2_process.sort(key= lambda q2_process: q2_process[1])
q3_process.sort(key= lambda q3_process: q3_process[1])

print "\t\tresult of queue 1"
print ''
if q1>=0:
	burst= []
	for i in range(q1+1):
		burst.append([])
		burst[i]= q1_process[i][2]
	final=q1_process[0][1]
	i=-1
	next_index= "true"
	total_waiting= 0
	total_turnaround= 0
	total_processes= q1+1
	while total_processes>0:
		if next_index== "true":
			i+=1
		if i>=total_processes:
			i=0
		next_index= "true"
		if burst[i] <= time:
			final+=burst[i]
			burst[i]=0
			waiting= final-q1_process[i][1]-q1_process[i][2]
			turnaround= final-q1_process[i][1]
			total_waiting+= waiting
			total_turnaround+= turnaround
			print "process ",q1_process[i][0]," arrive at ",q1_process[i][1]," & terminate at ",final
			print "waiting time of this process is ",waiting
			print "turnaround time of this process is ",turnaround
			print ''
		else:
			final+=time
			burst[i]-=time
		if burst[i]==0:
			burst.remove(burst[i])
			q1_process.remove(q1_process[i])
			total_processes-=1
			next_index= "false"

		if total_processes==0 :
			average_waiting= total_waiting/(q1+1)
			average_turnaround= total_turnaround/(q1+1)
			print "average waiting time is ",average_waiting
			print "average turnaround time is ",average_turnaround
			print ''

print "\t\tresult of queue 2"
print ''
if q2>=0:
	if q1==-1:
		start= 0
		arrival_sjf= 0
		finish= q2_process[0][1]
	else:
		start= final
		arrival_sjf= final
		finish= final+q2_process[0][1]
	total_waiting=0
	total_turnaround=0

	for i in range(q2+1):
		waiting = start-arrival_sjf
		turnaround = finish-arrival_sjf
		total_waiting+= waiting
		total_turnaround+= turnaround
		print "process ",q2_process[i][0]," arrive at ",arrival_sjf," & terminate at ",finish
		print "waiting time of this process is ",waiting
		print "turnaround time of this process is ",turnaround
		print ''
		start= finish
		if i<q2 :
			finish+= q2_process[i+1][1]

	print ''
	print "average waiting time: ",total_waiting/(q2+1)
	print "average turnaround time: ", total_turnaround/(q2+1)
	print ''

print "\t\tresult of queue 3"
print ''
if q3>=0:
	if q2==-1:
		if q1==-1:
			start= q3_process[0][1]
			finish= q3_process[0][2]
		else:
			start= final
			finish= final+q3_process[0][2]
	else:
		start= finish
		finish+= q3_process[0][2]
	total_waiting=0
	total_turnaround=0
	for i in range(q3+1):
		waiting = start-  q3_process[i][1]
		turnaround = finish- q3_process[i][1]
		total_waiting+= waiting
		total_turnaround+= turnaround
		print "process ",q3_process[i][0]," arrive at ",q3_process[i][1]," & terminate at ",finish
		print "waiting time of this process is ",waiting
		print "turnaround time of this process is ",turnaround
		print ''	
		start= finish
		if i<q3 :
			finish+= q3_process[i+1][2]
	print ''
	print "average waiting time: ",total_waiting/(q3+1)
	print "average turnaround time: ", total_turnaround/(q3+1)
