from util import EPS, format_arc

with open("../vocab/chars.syms", 'r') as file:
    data = file.read().replace('\n', '').replace('\t','')
import re
word1 = "".join(re.findall("[a-zA-Z]+", data))
file_name = 'alphabet.syms'
file_name=open("../vocab/alphabet.syms","w")
file_name.write(word1)

alphabet = word1
weight = {
    "delete": 1.0,
    "insert": 1.0,
    "sub": 1.0
}

# No edit
for l in alphabet:
    print(format_arc(0, 0, l, l))
    #print("0 0 {} {} {:.3f}".format(l, l, 0))

# Deletes: input character, output epsilon
for l in alphabet:
    print(format_arc(0, 0, l,"<eps>", weight["delete"]))
    #print("0 0 {} <eps> {:.3f}".format(l, weight["delete"]))

# Insertions: input epsilon, output character
for l in alphabet:
    print(format_arc(0, 0,"<eps>", l, weight["insert"]))
    #print("0 0 <eps> {} {:.3f}".format(l, weight["insert"]))

# Substitutions: input one character, output another
for l in alphabet:
    for r in alphabet:
        if l != r:
            print(format_arc(0, 0, l, r, weight["sub"]))
            #print("0 0 {} {} {:.3f}".format(l, r, weight["sub"]))

# Final state
print(0)
