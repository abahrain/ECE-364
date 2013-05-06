#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-31 11:23:51 -0500 (Thu, 31 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab04/validate_ip.bash $
#$Revision: 49667 $

F=$@

if (($# != 1))
then
    echo "Usage: validate_ip.bash <infile>"
    exit 1
elif [[ ! -e $1 ]] && [[ ! -r $1 ]]
then
    echo "error: $1 is not a readable file."
    exit 2
fi

while read ip
do
    if [[ "$ip" =~ ^(([0-1]?[0-9]?[0-9]|2?[0-5]?[0-5]|2[0-4][0-9])\.){3,3}([0-1]?[0-9]?[0-9]|2?[0-5]?[0-5]|2[0-4][0-9])$ ]]
    then
        echo "$ip - OK"
    else
        echo "$ip - BAD"
    fi
done < $1
exit 0
