# VMstats
VM Statistics
This is a Readme file for VM statistic gathering system and demo

Running the simulator Demo

Tested System: Ubuntu-15.04 					Python: 2.7.9

Files: 
1. vmrun.sh - Virtual Machine orchestrator, bash script
     usage -  ./vmrun.sh <running time in minutes>
2. Vms.py - Virtual machine class definition
3. vm-sim.py - single Virtual machine simulator, vmruns.sh invokes this 
4. vmser.py - Aggreagtor that collects stats data from every VMs. This is a well known server that every VM 
   informs its stats every minute. This is a push model.
   usage -  ./vmser.ph <running time in minutes>
   
   
To run the simulator,
1. copy all the files to a ubuntu (linux) directory
2. From one terminal window, run server side by giving
		./vmser.py 5
3. from another terminal window, run the VM simulator by giving
		./vmrun.sh 5
4. At the end, the server side will print the reclation recommendation. Some VMs are given a range under 10% during 
   simulation, so that every simulation run will have some VMs as under usage category.
   
 
 Design and some choices/recommendations(blueprint)
 
 1. The design currently hard coded with 5 simulated VMs. The Push model is prefered approach in this type of stats 
    collecting applications. The server acts as an aggregator that every CM client is reponsible for their own
	stats notification. 
2. The server is a single process model as to demonstrate a working solution. However, for scalabiliy consideration, 
   multi-process handling of either every VM clients message processing, some collection of message processing.
   This may be accomplished by
	a) On every connection request by a VM client, the server creates a process or thread and offloads the entire 
	   message processing that includes writing the stats into file in the disk. 
	b) On gathering some messages from some VM clients and keeping those messages in memory buffer, the server
	   can offload the processing of those messages and writing them to the disk file by creating a process or thread.
3. IP address of the VM client is the index of these VMs. The server desing creates and maintains log files
   for every VM by associating the IP address to the log file as it is easy to process in this case.
4. Also looked at some scalable frameworks like Tornado and Twisted
5. For simplicity of the code, only the happy path is assumed.
6. 

