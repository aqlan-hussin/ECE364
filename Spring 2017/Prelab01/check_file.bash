#! /bin/bash

filename=$1

if (( $# != 1 ))
then
	echo "Usage: ./check_file.bash <filename>"
else
	if [[ -e $filename ]]
	then
		echo "$filename exists"
	else
		echo "$filename does not exists"
	fi

	if [[ -d $filename ]]
	then
		echo "$filename is a directory"
	else
		echo "$filename is not a directory"
	fi

	if [[ -f $filename ]]
	then
		echo "$filename is an ordinary file"
	else
		echo "$filename is not an ordinary file"
	fi

	if [[ -r $filename ]]
	then
		echo "$filename is readable"
	else
		echo "$filename is not readable"
	fi

	if [[ -w $filename ]]
	then
		echo "$filename is writable"
	else
		echo "$filename is not writable"
	fi

	if [[ -x $filename ]]
	then
		echo "$filename is executable"
	else
		echo "$filename is not executable"
	fi
fi

exit 0
