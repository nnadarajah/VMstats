#!/bin/bash
#   This script launches muliple VM simulator scripts
#    On every iteration, the script creats 5 VM instance simulators.
#    The script takes time to run the simulation in minutes as commandline
#    input
#     Usage:    ./vmrun.sh 5 
#
	if [ $1 -le 0 ]
 	then
		echo "Usage ./vmrun.sh <min>"
		exit 1
	fi
	

	echo "VM simulation starts"
	/bin/rm *.log
	time_to_run=$(($1+1)) 	

	num_vm_sim=5     # number of VM simualtion
#
#	start the VM stats aggregator server 
#
#	./vmser.py  $time_to_run &
#	sleep 5
	j=1
	while [ $j -le $time_to_run ]
	   do
		i=1
		while [ $i -le $num_vm_sim ]
	        	do	
#
#     	every other VM is created to have usage under 10% and others 
#	under 100%	
#
				if [ $(($i % 2)) -le 0 ]
				then		
					random_range=10
				else
					random_range=100
				fi
				ip="10.10.1.$i"
				./vm-sim.py $ip  $random_range &
				i=$((i+1))	
			done
		sleep 10
		echo "VM simulation iteration $j is done" 
		j=$((j+1))	
		done
