from util import EPS, format_arc
import ast
from math import log10

file = open("../vocab/alphabet.syms","r")
alphabet = file.read()

def weight(num):
    return log10(1/num)

with open("../vocab/dictionary.txt", 'r') as file:
    data = file.read().strip()
frequencies = ast.literal_eval(data)

inf = 1000000
# No edit
for l in alphabet:
    print(format_arc(0, 0, l, l))

# Deletes: input character, output epsilon
for l in alphabet:
    if (l, '<eps>') not in frequencies:
        print(format_arc(0, 0, l,"<eps>", inf))
    else:    
        print(format_arc(0, 0, l,"<eps>", weight(frequencies[l, '<eps>'])))

# Insertions: input epsilon, output character
for l in alphabet:
    if ('<eps>', l) not in frequencies:
        print(format_arc(0, 0,"<eps>", l, inf))
    else:    
        print(format_arc(0, 0,"<eps>", l, weight(frequencies[('<eps>',l)])))

# Substitutions: input one character, output another
for l in alphabet:
    for r in alphabet:
        if l != r:
            if (l, r) not in frequencies:
                print(format_arc(0, 0, l, r, inf))
            else:
                print(format_arc(0, 0, l, r, weight(frequencies[l,r])))

# Final state
print(0)
