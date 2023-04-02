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

with open("./dictionary.txt", 'r') as file:
    data = file.read()
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
    #print("0 0 <eps> {} {:.3f}".format(l, weight["insert"]))

# Substitutions: input one character, output another
for l in alphabet:
    for r in alphabet:
        if l != r:
            if (l, r) not in frequencies:
                print(format_arc(0, 0, l, r, inf))
            else:
                print(format_arc(0, 0, l, r, weight(frequencies[l,r])))
            #print("0 0 {} {} {:.3f}".format(l, r, weight["sub"]))

# Final state
print(0)
