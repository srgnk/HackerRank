# Solution #1
echo "$(cut -c2,7)"

# Solution #2
#while IFS= read -r line ; do
#    echo "${line:1:1}${line:6:1}"
#done