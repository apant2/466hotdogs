import random
import os
import copy
 
#Create a nucleotide randomly
def create_nucleotide():
    num = int(random.randint(0,100000)%4)
    if(num==0):
        return 'A'
    if(num==1):
        return 'T'
    if(num==2):
        return 'G'
    if(num==3):
        return 'C'
 
#Generate a random nucleotide sequence of length L
def generate_sequences(length):
    out=''
    for i in range(length):
        out+=create_nucleotide()
    return out
 
#Test if the entered value is the same as a random one, and return the random one
def change_nucleotide(nucleotide_value):
    a=create_nucleotide()
    if(a==nucleotide_value):
        change_nucleotide(input)
    else:
        return a
 
#Genereate num_seq random sequences each of length len_seq
def generate_multiple_sequences(num_seq, len_seq):
    sequences=[]
    for i in range(num_seq):
        sequences.append(generate_sequences(len_seq))
    return sequences
#3
def random_variable_DNA_seq(seq_len, num_var_pos):
    seq = generate_sequences(seq_len)
    marker_positions = var_markers(seq_len, num_var_pos)
    return seq, marker_positions
   
def var_markers(seq_len, num_var_pos):    
    if(num_var_pos>=seq_len):
       mark = ["*"]*seq_len
       return mark
    mark = [""]*seq_len
    if (num_var_pos==0):
        return mark
    rand_pos = random.sample(range(seq_len), num_var_pos)
    for val in rand_pos:
        mark[val]="*"
    return mark
 
#4
def binding_sites(seq, marker_positions1, num_sites):
    marker_positions = copy.deepcopy(marker_positions1)
    if num_sites<=len(seq):
        pos = random.sample(range(len(seq)), num_sites)
    else:
        pos = [random.choice(list(range(len(seq)))) for _ in range(num_sites)]
    for elem in pos:
        if(marker_positions[elem]=="*"):
            marker_positions[elem]="b*"
        else:
            marker_positions[elem]="b"
    return marker_positions
 
#Number 5; planting. Take inpit from sequences
def plant_sampled_site(sequences, motif, direc=''):
    loc_planted=[]
    out=[]
    len_motif = len(motif)
    for seq in sequences:
        max_pos = len(seq)-len_motif+1
        pos = round(random.uniform(0,max_pos))
        seq_final = seq[:pos]+motif+seq[pos+len_motif:]
        loc_planted.append(str(pos))
        #final_seq = ''.join(seq)
        out.append(seq_final)
   
    f = open(direc+'/sites.txt', 'w')
    i=0
    for seq in sequences:
        f.write(loc_planted[i])
        f.write("\n")
        i+=1
    f.close()
    return out
 
def sc_to_seq(sequences, direc=''):
    f = open(direc+'/sequences.fa','w')
    i=0
    for seq in sequences:
        f.write(">seq"+str(i))
        f.write("\n")
        f.write(seq)
        f.write("\n")
        i+=1
    f.close()
 
def planted_loc(marker_positions, direc=""):
    a = open(direc+'/sites.txt', 'w')
    
    for seq in sequences:
        c = seq.index("b*")
        a.write(c)
    a.close()
   
def motif_output(seq, a, direc=""):
    print(seq)
    print(a)
    length = len(seq)
    name = "MOTIF1"
    out=[]
    i=0
    for elem in seq:
        if(a[i]=="*"):
            out.append("*")
        else:
            out.append(elem)
        i+=1
    final_out = ''.join(out)
    f = open(direc+"/motif.txt", 'w')
    f.write(name+" "+str(length)+" "+final_out)
    f.close()
 
def motif_len_out(seq, direc=""):
    f = open(direc+"/motiflength.txt", 'w')
    f.write(str(len(seq)))
    f.close()
 
#Values to use to generate set
ML=8
NM=4
SL=500
SC=10
 
#Will generate 1 (and only 1) data with set given paramters
 
def create_ds(ML, NM, SL, SC, direc=''):
    direc="/"+direc
    current_dir = os.getcwd()
    if(direc != '' and not os.path.exists(current_dir+direc)):
        os.mkdir(current_dir+direc)
   
    d_out = current_dir+direc
   
    random_sequences = generate_multiple_sequences(SC, SL)
    seq, markers= random_variable_DNA_seq(ML, NM)
    marker_positions = binding_sites(seq, markers, SC)
 
    #Creates the actual files
    random_sequences = plant_sampled_site(random_sequences,seq, d_out)
    sc_to_seq(random_sequences, d_out)
    motif_output(seq, markers, d_out)
    motif_len_out(seq, d_out)

    
def create_all():
    i=0
    ML=8
    NM=3
    SL=500
    SC=10

    NM_arr=[0,1,2]
    ML_arr=[6,7,8]
    SC_arr = [5, 10, 20]
    
    for a in range(10):
        for nm in NM_arr:
            create_ds(ML, nm, SL, SC, direc=str(i))
            i+=10
        for ml in ML_arr:
            create_ds(ml, NM, SL, SC, direc=str(i))
            i+=1
        for sc in SC_arr:
            create_ds(ML, NM, SL, sc, direc=str(i))
            i+=1