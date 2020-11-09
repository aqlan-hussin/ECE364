#! /bin/bash

filename=$1

if (( $# == 0 ))
then
	echo "usage: sensor_sum.sh log"
	exit 0
fi

if (( $# != 1 ))
then
	echo "Error: Provide ONE filename"
	exit 0
fi

if [[ ! -r filename ]]
then
	echo "error: $filename is not a readable file!"
	exit 0
fi

while read line
do
	i=1
	total=0
	for word in $line
	do
		if (( i == 1 ))
		then
			printf "%0.2s " $word
		else
			let total=total+$word
			if (( i == 4 ))
			then
				printf "$total\n"
			fi
		fi
		let i=i+1
	done
done < $1

exit 0
