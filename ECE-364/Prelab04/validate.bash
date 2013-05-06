#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-29 20:56:59 -0500 (Tue, 29 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab04/validate.bash $
#$Revision: 49516 $

F=$@
IFS='_'

if (($# != 1))
then
    echo "Usage: validate.bash <filename>"
    exit 1
elif [[ ! -e $1 ]] && [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable"
    exit 1
fi

while read -d'_'  word
do
    if [[ "$word" =~ ^([A-Z][a-z]*)$ ]]
    then
        echo ""$word" is capitalized."
    elif [[ "$word" =~ ^([a-z]*)$ ]]
    then
        echo ""$word" is a lower case."
    elif [[ "$word" =~ ^([A-Za-z]+)$ ]]
    then
        echo ""$word" is mixed case."
    elif [[ "$word" =~ ^([a-z0-9]+)$ ]]
    then
        echo ""$word" is alphanumeric."
    else
        echo ""$word" is weird!"
    fi
done<$1

exit 0
