# Solution 1
cut -d' ' -f4
# Solution 2
#awk -F'\t' '{print $1, $2, $3}'