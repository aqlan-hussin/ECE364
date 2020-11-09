#! /bin/bash

filename=$1

if (( $# != 1 ))
then
	echo "Error: Only one filename!"
fi

if [[ -e $filename ]] && [[ -r $filename ]]
then
	cat -n $filename
else
	echo "Cannot read $filename"
fi

exit 0
	

