import math
import numpy as np
# step 3.1

def convert_motif(filename):
    with open(filename, 'r') as f:
        mpwm = f.read().splitlines()
    with open("sequences.fa", 'r') as f:
        seq = f.read().splitlines()
    
    mdata = mpwm[0].split()
    num_seq = len(seq)/2
    ML = int(mdata[1])
    motif = str(mdata[2])
    motif_matrix = np.zeros((ML,4))
    for i in range(ML):
        if motif[i]=='A':
            motif_matrix[i, 0] = num_seq
        elif motif[i]=='C':
            motif_matrix[i, 1] = num_seq
        elif motif[i]=='G':
            motif_matrix[i, 2] = num_seq
        elif motif[i]=='T':
            motif_matrix[i, 3] = num_seq
        elif motif[i]=='*':
            motif_matrix[i, 0] = num_seq/4
            motif_matrix[i, 1] = num_seq/4
            motif_matrix[i, 2] = num_seq/4
            motif_matrix[i, 3] = num_seq/4
    motif_matrix = motif_matrix/10
    of = open("powermotif.txt", 'w')
    for i in range(ML):
        of.write(str(motif_matrix[i, 0]) + " " + str(motif_matrix[i, 1]) + " " + str(motif_matrix[i, 2]) + " " + str(motif_matrix[i, 3]) + "\n")


def relative_entropy(filename1, filename2):
    convert_motif("motif.txt")
    with open(filename1, 'r') as f:
        pwm = f.read().splitlines()
    pwm.pop(0) # don't need >PMOTIF
    pwm.pop(-1) # don't need <
    with open(filename2, 'r') as f:
        motif_modified = f.read().splitlines()
    
<<<<<<< HEAD
=======

#### Start of implementation of REM from online formula
    for a in range(ML):
        for b in range(4):
            relative_entropy += PWM_predicted[a][b] * math.log(PWM_predicted[a][b] / PWM_actual[a], 2)
#### END REM online formula implementation

>>>>>>> FETCH_HEAD
=======
>>>>>>> origin/master
    rel_ent = [] # store relative entropies of each position
    for i in range(len(pwm)):
        sum = 0 # relative entropy at a position
        pwm_line = pwm[i].split()
        motif_line = motif_modified[i].split()
        for j in range(4): # relative entropy at a position is sum of probabilities at A,C,G,T
            p = float(pwm_line[j]) # p is originally a string. need to convert to float
            q = float(motif_line[j])
            if p==0:
                p = 1e-3 # small value. logarithms cannot take 0.
            if q==0:
                q = 1e-3 # small value. logarithms cannot take 0.
            sum += p*math.log(p/q,2)
        rel_ent.append("{0:.2f}".format(sum))
    
    re_file = open("relative_entropy.txt", 'w')
    for re_line in rel_ent:
        re_file.write(str(re_line) + "\n")


relative_entropy("predictedmotif.txt", "powermotif.txt")
