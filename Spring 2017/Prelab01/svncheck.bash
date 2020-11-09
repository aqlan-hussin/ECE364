#! /bin/bash

x='N'

while read line
do	
	status=$(svn status $line)
	#echo $status
	if [[ ! -z $status ]]
	then
		echo "changes found"
		if [[ -e $line ]]
		then	
			if [[ ! -x $line ]]
			then
				read -p "Do you want the file to be executable? [Y/N]: " x
				if (( x == 'Y' ))
				then
					chmod +x $line
				fi
			fi
			svn add $line		
		else
			echo "Error: File $line appears to not exist here or in svn"		
		fi
	else
		if [[ ! -x $line ]]
		then
			svn propset svn:executable ON $line
		fi	
	fi
done < file_list

svn commit -m "Auto-commiting code"

exit 0
