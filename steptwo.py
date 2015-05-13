# this function scores matches as 1, mismatches as 0.

import distance
'''
def score(a, b):
    matches = 0
    merged_list = list(zip(a, b))
    for i in range(len(merged_list)):
        if a[i] == b[i]:
            matches += 1
    return matches'''

def score(a, b):
    return len(a) - distance.hamming(a,b)

def pwm(motif_list, motif_len):
    num_A = 0
    num_C = 0
    num_G = 0
    num_T = 0
    pmotif_rows = []
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
        pmotif_rows.append("%d %d %d %d\n" % (num_A, num_C, num_G, num_T))

    return pmotif_rows

def find_motifs():
    with open("motiflength.txt", 'r') as f:
        mot_len = f.readlines()
    with open("sequences.fa", 'r') as f:
        seq = f.read().splitlines()
    ML = int(mot_len[0])
    m = [""] * len(seq)
    pred_sites = [""]*len(seq)
    seq_size = len(seq[1])
    m[0] = "X" * ML
    m[1] = "Y" * ML
    for i in range(0, seq_size-ML + 1):
        for j in range(0, seq_size-ML + 1):
            test_motif_A = seq[1][i:i + ML] # the slice represents the size of the motif
            test_motif_B = seq[3][j:j + ML]
            if score(test_motif_A, test_motif_B) > score(m[0], m[1]):
                m[0] = test_motif_A
                m[1] = test_motif_B
                pred_sites[0] = i
                pred_sites[1] = j

    for i in range(5, len(seq), 2): # we iterate all sequences beyond the first two
        m[i] = "V" * ML
        for j in range(0, seq_size-ML+1):
            tmot = seq[i][j:j + ML]
            if score(m[0], tmot) >= score(m[0], m[i]):
            # maybe use this? and score(m[1], tmot) >= score(m[1], m[i])
                m[i] = tmot
                pred_sites[i] = j

    m = list(filter(None, m))
    pred_sites = list(filter(None, pred_sites))
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
