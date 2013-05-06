#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-17 00:02:17 -0500 (Thu, 17 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab02/svncheck.bash $
#$Revision: 48315 $

FILE=$(head file_list)

if ( ! $(svn status $FILE) = '')
then
    read -p "Do you want to add $FILE to svn?" test
    if $test = 'yes'
    then
        svn add $FILE
    fi
elif [[ ! -e $FILE ]]
then
    echo "ERROR: File $FILE appears to not exist here or in svn."

fi

exit 0
