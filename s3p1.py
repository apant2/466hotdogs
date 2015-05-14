import math

# step 3.1
def relative_entropy(filename):
    with open(filename, 'r') as f:
        pwm = f.read().splitlines()
    pwm.pop(0) # don't need >PMOTIF
    pwm.pop(-1) # don't need <

    rel_ent = [] # store relative entropies of each position
    for i in range(len(pwm)):
        sum = 0 # relative entropy at a position
        pwm_line = pwm[i].split()
        for j in range(4): # relative entropy at a position is sum of probabilities at A,C,G,T
            p = float(pwm_line[j]) # p is originally a string. need to convert to float
            if p==0:
                p = 1e-10 # small value. logarithms cannot take 0.
            sum += p*math.log(p/0.25)
        rel_ent.append(sum)

    print(rel_ent)

relative_entropy("predictedmotif.txt")