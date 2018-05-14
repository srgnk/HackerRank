read string

res=$(echo "$string" | bc -l)

printf "%.3f" "$res"