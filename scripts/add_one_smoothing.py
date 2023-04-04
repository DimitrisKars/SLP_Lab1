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
    else:
        f = frequencies[l, '<eps>']
        p = probability(f, N, V)
        count_prob += p
        print(format_arc(0, 0, l,"<eps>", weight(p)))

# Insertions: input epsilon, output character
for l in alphabet:
    if ('<eps>', l) not in frequencies:
        count_zero += 1
        zero.append(('<eps>', l))
    else:    
        f = frequencies[('<eps>',l)]
        p = probability(f, N, V)
        count_prob += p
        print(format_arc(0, 0,"<eps>", l, weight(p)))

# Substitutions: input one character, output another
for l in alphabet:
    for r in alphabet:
        if l != r:
            if (l, r) not in frequencies:
                count_zero += 1
                zero.append((l, r))
            else:
                f = frequencies[l,r]
                p = probability(f, N, V)
                count_prob += p
                print(format_arc(0, 0, l, r, weight(p)))

remaining = (1 - count_prob)/count_zero
for z in zero:

    print(format_arc(0, 0, z[0], z[1], weight(remaining)))

# Final state
print(0)

