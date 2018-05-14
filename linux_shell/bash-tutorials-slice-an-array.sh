readarray array

for i in {3..7} ; do
    echo -ne ${array[${i}]}
    echo -ne " "
done