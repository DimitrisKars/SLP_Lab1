f=open("words_only.syms","r")
dictionary=f.readlines()
dictionary = [s.rstrip() for s in dictionary]
