#! /bin/bash

if (( $# != 1 ))
then
	echo "Usage: yards.bash <filename>"
	exit 1
fi

if [[ ! -r $1 ]]
then		
	echo "Error: $1 is not readable"
	exit 2
fi

largest=0

while read line
do
	j=-1
	total=0
	var=0
	sq=0
	for word in $line
	do
		if (( j == -1 ))
		then
			printf "%s schools averaged " $word
		else
			(( total=total+$word ))
			arr[j]=$word
		fi
		(( j=j+1 ))
	done
	(( avg=$total/$j ))
	if (( $avg > $largest ))
	then
		largest=$avg
	fi
	for (( i=0; i < j; i++ ))
	do
		(( sq=${arr[i]}-$avg ))
		(( sq=$sq*$sq ))
		(( var=var+$sq ))
	done
	(( var=var/j ))
	echo "$avg yards receiving with a variance of $var"
done < $1

echo "The largest average yardage was $largest"

exit 0
