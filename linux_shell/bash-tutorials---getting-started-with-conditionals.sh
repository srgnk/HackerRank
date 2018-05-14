read answer

if [[ ${answer,,}  == 'y' ]] ; then
    echo 'YES'
elif [[ ${answer,,} == 'n' ]] ; then
    echo 'NO'
fi