#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-31 10:56:00 -0500 (Thu, 31 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab04/validate_motherboards.bash $
#$Revision: 49658 $

F=$@

if (($# != 1))
then
    echo "Usage: validate_motherboards.bash <infile>"
    exit 1
elif [[ ! -e $1 ]] && [[ ! -r $1 ]]
then
    echo "error: $1 is not a readable file."
    exit 2
fi


while read man mod price
do
    if [[ "$price" =~ ^[0-9]+(\.[0-9]+)?$ ]]
    then
        if [[ "$man" =~ "ASUS" ]]
        then
            if [[ "$mod" =~ ^P[0-9](Z|B|F)(1[0-9][0-9]|2[0-9][0-9]|3[0-2][0-9]|33[0-3])(\-(V|X))?$ ]]
            then
                echo "$man $mod $price"
            else
                echo "Model number $mod is not valid for the manufacturer $man"
            fi
        elif [[ "$man" =~ "Gigabyte" ]]
        then
            if [[ "$mod" =~ ^G(A|B|C|X)(\-(7[0-9]))L?(M|P)T?U?(\-(I|A))[0-9]+$ ]]
            then
                echo "$man $mod $price"
            else
                echo "Model number $mod is not valid for the manufacturer $man"
            fi 
        elif [[ "$man" =~ "MSI" ]]
        then
            if [[ "$mod" =~ ^("FM1"|"FM2"|"FM3"|"FMJ")(\-(A))(5[0-9]|6[0-9]|7[0-9])L?(M|P)?(\-([A-Z]{3}))$ ]]
            then
                echo "$man $mod $price"
            else
                echo "Model number $mod is not valid for the manufacturer $man"
            fi 
        else
            echo "Unknown manufacturer $man"
        fi
    else
        echo "Invalid price field for $mod"
    fi
done < $1

exit 0
