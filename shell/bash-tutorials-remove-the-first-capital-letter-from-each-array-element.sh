arr=( $(cat) )

for elem in ${arr[@]} ; do
    echo -ne ".${elem:1} "
done