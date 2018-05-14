read len
readarray arr

res=0

for elem in ${arr[@]} ; do
    res=$(( res ^ elem ))
done

echo "$res"