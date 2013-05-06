#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-17 00:03:42 -0500 (Thu, 17 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab02/exist.bash $
#$Revision: 48317 $

File=$@

if [[ -e $File ]] && [[ -r $File ]]
then
    echo "File $File is readable!"
else
    touch $File
fi

exit 0
