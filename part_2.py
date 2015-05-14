# this function scores matches as 1, mismatches as 0.
import numpy as np
import time

def score(seq, num_seq, DNA, ML):  # number of sequences we are comparing in profile matrix
    profile_matrix = np.zeros((4, ML))
    occurrences = np.zeros(ML)
    consensus_score = 0
    for i in range(ML):
        for j in range(num_seq):  # up to how many sequences
            if DNA[j][int(seq[j])+i] == 'A':  # seq[j] is motif start index
                profile_matrix[0, i] += 1
            elif DNA[j][int(seq[j])+i] == 'C':
                profile_matrix[1, i] += 1
            elif DNA[j][int(seq[j])+i] == 'G':
                profile_matrix[2, i] += 1
            elif DNA[j][int(seq[j])+i] == 'T':
                profile_matrix[3, i] += 1

for k in range(ML):  # k represents the current position within a motif
    for x in range(4):  # x represents which letter A,C,G,T we're iterating over
        if profile_matrix[x, k] > occurrences[k]:
            occurrences[k] = profile_matrix[x, k]
        consensus_score += occurrences[k]
    
    return consensus_score
def pwm(motif_list, ML): # seq is list of all ideal motifs. ML is motif length
    profile_matrix = np.zeros((4, ML))
    for i in range(ML): # go through each position in motif
        for j in range(len(motif_list)):  # set of all motifs
            if motif_list[j][i] == 'A':  # seq[j] is motif start index
                profile_matrix[0, i] += 1
            elif motif_list[j][i] == 'C':
                profile_matrix[1, i] += 1
            elif motif_list[j][i] == 'G':
                profile_matrix[2, i] += 1
            elif motif_list[j][i] == 'T':
                profile_matrix[3, i] += 1

return profile_matrix.transpose()
# Inputs the list of all motifs (one motif per sequence) as motif_list,
# and the integer of motif length (each motif has same length) as motif_len
# Returns the position weight matrix

#  The actual algorithm.
def find_motifs():
    with open("motiflength.txt", 'r') as f:
        mot_len = f.readlines()
    with open("sequences.fa", 'r') as f:
        seq = f.read().splitlines()
    seq = [elem for elem in seq if len(elem) == 500]  # filter out the >seq w/e lines.
    ML = int(mot_len[0]) #  cast mot_len to an integer
    best_motif = np.zeros(len(seq))
    s = np.zeros(len(seq))
    seq_size = len(seq[0])
    best_score = score(best_motif, 2, seq, ML)
    for i in range(seq_size-ML + 1):
        s[0] = i
        for j in range(seq_size-ML + 1):
            s[1] = j
            if score(s, 2, seq, ML) > score(best_motif, 2, seq, ML): # if new motif score > score of current motif score, replace current with new
                best_motif[0] = s[0]
                best_motif[1] = s[1]

s[0] = best_motif[0]
    s[1] = best_motif[1]
    
    for i in range(2, len(seq)): # go through set of all sequences
        for j in range(seq_size-ML+1): # go through potential motifs in each sequence
            s[i] = j
            sc = score(s, i+1, seq, ML)
            if sc > best_score:
                best_score = sc
                s[i] = j
                best_motif[i] = j

psites = open("predictedsites.txt", 'w')
    for i in range(len(best_motif)):
        psites.write(str(best_motif[i])+'\n')

pmotif = open("predictedmotif.txt", 'w')
    pmotif.write(">PMOTIF " + str(ML) + "\n")
    pwm_rows = pwm(seq, ML)
    pwm_rows = pwm_rows/len(seq)
    for i in range(len(pwm_rows)):
        pmotif.write(str(pwm_rows[i, 0]) + " " + str(pwm_rows[i, 1]) + " " + str(pwm_rows[i, 2]) + " " + str(pwm_rows[i, 3]) + "\n")
pmotif.write("<")
start = time.time()
find_motifs()
end = time.time()

print(end - start)