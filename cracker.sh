#!/bin/bash

# Check if the number of arguments provided is correct
if [ $# -ne 1 ]; then
    echo "Usage: $0 <number of hashes to generate>"
    exit 1
fi

# generate wordlist
if [ -e "wordlists/combined.txt" ]; then
    echo "wordlist exists"
else
    echo "creating wordlist"
    python3 combiner.py
fi


# clear files
echo "" > hashes/randomHashes.json
echo "" > hashes/sha512.txt
echo "" > hashes/solution.txt

#generate hashes
python3 genRandomThreaded.py $1
python3 parseFromJson.py

#crack hashes
hashcat -m 1700 -O -o hashes/solution.txt hashes/sha512.txt -a 6 wordlists/combined.txt ?d?d

#check solution
python3 solutionCheck.py