#!/usr/bin/env bash

# Solution #1
echo "$(cut -c1-4)"

# Solution #2
#while IFS= read -r line ; do
#    echo "${line:0:4}"
#done