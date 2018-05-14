# solution 1
#uniq -c | cut -c7-

# solution 2
uniq -c | sed -e 's/^[ \t]*//'