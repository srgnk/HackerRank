read all

for ((i=0;i<$all;i++)) ; do
    read num
    sum=$((sum + num))
done

result=$(echo "$sum/$all" | bc -l)

printf "%.3f" "$result"