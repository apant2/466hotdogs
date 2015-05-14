
#Step 3 of CS 466 Project: Evaluating the motif finder on the benchmark

import time
import os
import part_1 as first
import part_2 as second
import csv


first.create_all()

rootdir = os.getcwd() #Rootdir is directory where the folders for the datasets are, and the three files are located

#Arrays used in the program
time_per_set=[]
count_arr=[]

for subdir, dirs, files in os.walk(rootdir):
    for dir_name in dirs:
        os.chdir(rootdir+"/"+dir_name+"/")

        #3)	Running	time.
        start_time = time.monotonic()
        second.find_motifs()
        end_time = time.monotonic()
        delta = end_time - start_time
        time_per_set.append(delta)

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
        count = count(overlap)
        count_arr.append(count)
        #output result to some file



os.chdir(rootdir)
resultFile = open("runtimedata.csv",'wb')
wr = csv.writer(resultFile, delimiter=';')
for delta in time_per_set:
    wr.writerows([delta])

resultFile = open("countdata.csv", 'wb')
wr = csv.writer(resultFile, delimiter=';')
for count in count_arr:
    wr.writerows([count])

#do some analysis or something