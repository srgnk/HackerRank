#echo "${line:2:1}" <(/dev/stdin)
echo "$(cut -c3)"
#while IFS='' read -r line ; do
#    echo "${line:2:1}"
#done