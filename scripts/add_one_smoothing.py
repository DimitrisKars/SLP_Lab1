from util import EPS, format_arc
import ast
from math import log

with open("../vocab/chars.syms", 'r') as file:
    data = file.read().replace('\n', '').replace('\t','')
import re
word1 = "".join(re.findall("[a-zA-Z]+", data))
file_name = 'alphabet.syms'
file_name=open("../vocab/alphabet.syms","w")
file_name.write(word1)

alphabet = word1
def weight(num):
    return log(1/num)

def probability(f, N, V):
    return (f+1)/(N+V)
    

with open("./dictionary.txt", 'r') as file:
    data = file.read()
frequencies = ast.literal_eval(data)

inf = 1000000
# No edit
for l in alphabet:
    print(format_arc(0, 0, l, l))

count_zero = 0
count_prob = 0
zero = []
V = len(frequencies)
N = 0

for key, item in frequencies.items():
    N += item
 
# Deletes: input character, output epsilon
for l in alphabet:
    if (l, '<eps>') not in frequencies:
        count_zero += 1
        zero.append((l, '<eps>'))
        #print(format_arc(0, 0, l,"<eps>", inf))
    else:
        f = frequencies[l, '<eps>']
        p = probability(f, N, V)
        count_prob += p
        print(format_arc(0, 0, l,"<eps>", p))

# Insertions: input epsilon, output character
for l in alphabet:
    if ('<eps>', l) not in frequencies:
        count_zero += 1
        zero.append(('<eps>', l))
        #print(format_arc(0, 0,"<eps>", l, inf))
    else:    
        f = frequencies[('<eps>',l)]
        p = probability(f, N, V)
        count_prob += p
        print(format_arc(0, 0,"<eps>", l, p))
    #print("0 0 <eps> {} {:.3f}".format(l, weight["insert"]))

# Substitutions: input one character, output another
for l in alphabet:
    for r in alphabet:
        if l != r:
            if (l, r) not in frequencies:
                count_zero += 1
                zero.append((l, r))
                #print(format_arc(0, 0, l, r, inf))
            else:
                f = frequencies[l,r]
                p = probability(f, N, V)
                count_prob += p
                print(format_arc(0, 0, l, r, p))
            #print("0 0 {} {} {:.3f}".format(l, r, weight["sub"]))

remaining = (1 - count_prob)/count_zero
for z in zero:

    print(format_arc(0, 0, z[0], z[1], remaining))

# Final state
print(0)

