# this function scores matches as 1, mismatches as 0.

import distance
def num_lines(filename):
    return sum(1 for line in open(filename))
def score(a, b):
    return len(a) - distance.hamming(a,b) #hamming is the number of differences between two strings

#Inputs the list of all motifs (one motif per sequence) as motif_list, and the integer of motif length (each motif has same length) as motif_len
#Returns the position weight matrix
def pwm(motif_list, motif_len):
    num_A = 0 #number of A nucleotides. Similar for next three lines
    num_C = 0
    num_G = 0
    num_T = 0
    pmotif_rows = []
    #Fills in the position weight matrix. Traverses every character in all the motifs in motif_list
    for i in range(len(motif_list)):
        for j in range(motif_len):
            if motif_list[i][j]=='A':
                num_A += 1
            elif motif_list[i][j]=='C':
                num_C += 1
            elif motif_list[i][j]=='G':
                num_G += 1
            elif motif_list[i][j]=='T':
                num_T += 1
        #After going through a motif, add the num values to the first row of the posittion weight matrix
        pmotif_rows.append("%d %d %d %d\n" % (num_A, num_C, num_G, num_T))
    
    return pmotif_rows

#The actual algorithm.
def find_motifs():
    with open("motiflength.txt", 'r') as f:
        mot_len = f.readlines()
    with open("sequences.fa", 'r') as f:
        seq = f.read().splitlines()
    seq = [elem for elem in seq if len(elem) ==500] # filter out the >seq w/e lines.
    ML = int(mot_len[0]) #cast mot_len to an integer
    m = [""] * len(seq)
    pred_sites = [""]*len(seq)
    seq_size = len(seq[1])
    m[0] = "" * ML # initialize so score() runs
    m[1] = "" * ML
    for i in range(0, seq_size-ML + 1):
        for j in range(0, seq_size-ML + 1):
            test_motif_A = seq[0][i:i + ML] # the slice represents the size of the motif
            test_motif_B = seq[1][j:j + ML]
            if score(test_motif_A, test_motif_B) > score(m[0], m[1]): # if new motif score greater than score of current motif score, replace current with new
                m[0] = test_motif_A
                m[1] = test_motif_B
                pred_sites[0] = i
                pred_sites[1] = j

for i in range(2, len(seq)): # go through set of all sequences
    m[i] = "V" * ML
        for j in range(0, seq_size-ML+1): # go through potential motifs in each sequence
            tmot = seq[i][j:j + ML] # current best motif match
            if score(m[0], tmot) > score(m[0], m[i]):
                # maybe use this? and score(m[1], tmot) >= score(m[1], m[i])
                m[i] = tmot
                pred_sites[i] = j

print(m)
    print(pred_sites)
    
    psites = open("predictedsites.txt", 'w')
    for i in range(len(pred_sites)):
        psites.write(str(pred_sites[i])+'\n')
    
    pmotif = open("predictedmotif.txt", 'w')
    pmotif.write(">PMOTIF " + str(ML) + "\n")
    pwm_rows = pwm(m, ML)
    for i in range(len(pwm_rows)):
        pmotif.write(pwm_rows[i])
    pmotif.write("<")

find_motifs()
