readarray array
declare -a output=( ${array[@]/*[a,A]*/} )

echo ${output[@]}