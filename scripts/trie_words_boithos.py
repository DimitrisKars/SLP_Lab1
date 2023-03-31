f=open("words_only.syms","r")
dictionary=f.readline()
dictionary = [s.rstrip() for s in dictionary]
for word in dictionary:
    print(f'{
