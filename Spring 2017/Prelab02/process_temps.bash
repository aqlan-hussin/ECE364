#! /bin/bash

if (( $# != 1 ))
then
	echo "Usage: process_temps.bash <input file>"
	exit 1
fi

if [[ ! -r $1 ]]
then
	echo "Error: $1 is not a readable file"
	exit 2
fi

i=1
n=-1

while read line
do
	total=0
	j=0	
	if (( $i == 1 ))
	then
		for word in $line
		do
			(( n = n+1 ))
		done
	else
		for word in $line
		do
			if (( $j == 0 ))
			then
				time=$word
			else
				(( total=total+$word ))
			fi
			(( j=j+1 ))
		done
		(( avg=$total/n ))
		echo "Average temperature for $time was $avg C."
	fi
	(( i=i+1 ))
done < $1

exit 0