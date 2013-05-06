#! /bin/bash

echo
echo
echo "*** IMPORTANT ***"
echo "Please read the following message before you make use of this script!"
echo "https://engineering.purdue.edu/ee364/lectures/regex_example_notes.txt"
echo "*** IMPORTANT ***"
echo 
echo

echo "Use ctrl+c to quit at any time."
echo

read -p "Enter your regex: " regex

while [[ -z $regex ]]
do
    echo "An empty regex is not very interesting..."
    read -p "Enter your regex: " regex
done

if [[ ${regex:0:1} != "^" && ${regex:${#regex}-1:1} != "$" ]]
then
    echo "Note: Your regex will preform a search, not an exact match!"
fi

while (( 1 == 1 ))
do
    read -p "String: " str
    
    if [[ $str =~ $regex ]]
    then
	echo "\"$str\" matches!"
    else
	echo "\"$str\" does not match!"
    fi
    
done

exit 0
