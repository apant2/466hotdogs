#Step 3 of CS 466 Project: Evaluating the motif finder on the benchmark

import time
import os

rootdir = '/' #Rootdir is directory where the folders for the datasets are

for subdir, dirs, files in os.walk(rootdir):
    for dir_name in dirs:
        
        
        #1)	Convert	the	motif	in	motif.txt	to	a	PWM	format	and	compute	relative	entropy
        #between	“motif.txt”	and	“predictedmotif.txt”	(search	the	web	for	what	“relative
        #entropy”	means).
        
        
        #2)	Number	of	overlapping	positions	or	overlapping	sites	between	“sites.txt”	and
        #“predictedsites.txt”.
        a=[]
            b=[]
            with open('sites.txt', 'r') as s:
                for line in s:
                    val=line.strip()
                    a.append(int(val))
        with open('predictedsites.txt', 'r') as p:
            for line in p:
                val=line.strip()
                    b.append(int(val))
        
            overlap = set(a) & set(b)
            #count the overlap set or something
            #output result to some file
            
            
            #3)	Running	time.
            start_time = time.monotonic()
            #Run algorithm on one directory
    end_time = time.monotonic()
#output change in times to a file that will be analyzed