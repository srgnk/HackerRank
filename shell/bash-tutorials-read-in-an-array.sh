readarray array
for el in ${array[@]} ; do 
    echo -ne "$el "
done
echo