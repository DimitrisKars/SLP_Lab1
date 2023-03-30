declare -i w=0
while read p; do
  python mkfstinput.py $p > "$(printf "./fsts_for_words/word_fst%s" $((w+1)))"
  ((w=w+1))
done <<<$(awk 'BEGIN { FS="\t" } { print $1 }' words.syms)





