from util import EPS, format_arc

alphabet = "abcdefg"

weight = {
    "delete": 1.0,
    "insert": 1.0,
    "sub": 1.5
}

# No edit
for l in alphabet:
    print(format_arc(0, 0, l, l))

# Deletes: input character, output epsilon
for l in alphabet:
    print(format_arc(0, 0, l,"<eps>", weight["delete"]))

# Insertions: input epsilon, output character
for l in alphabet:
    print(format_arc(0, 0,"<eps>", l, weight["insert"]))

# Substitutions: input one character, output another
for l in alphabet:
    for r in alphabet:
        if l != r:
            print(format_arc(0, 0, l, r, weight["sub"]))

# Final state
print(0)
