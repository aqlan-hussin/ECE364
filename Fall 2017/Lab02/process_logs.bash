#! /bin/bash

#---------------------------------------
# $Author: ee364a16 $
# $Date: 2017-08-30 13:01:02 -0400 (Wed, 30 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

if (( $# != 1 ))
then
	echo "Usage: process_logs.bash <input file>"
	exit 1
fi

if [[ ! -r $1 ]]
then
	echo "Error: $1 is not a readable file."
	exit 2
fi

n=0
j=0
exec 4> $1.out

while read line
do
	total=0
	i=-1
	if (( n == 0 ))
	then
		array=($line)
		(( n = ${#array[@]} - 1 ))
	else
		for word in $line
		do
			if (( $i == -1 ))
			then
				timeval=$word
			else
				(( total = total + $word ))
				arr[$i]=$word
			fi
			(( i = i + 1 ))
		done
		avg=$(echo "scale=2; $total/$n" | bc)
		IFS=$'\n' sorted=($(sort <<<"${arr[*]}"))
		unset IFS
		if (( n % 2 == 0 ))
		then
			(( num = $n/2 ))
			(( med = (${sorted[$num]} + ${sorted[$num-1]}) ))
			median=$(echo "scale=2; $med/2" | bc)
		else
			(( num = ($n+1)/2 ))
			(( med=${sorted[$num-1]} ))
			median=$(echo "scale=2; $med/1" | bc)
		fi
		echo "Average temperature for time $timeval was $avg C." >&4
		echo "Median temperature for time $timeval was $median C." >&4
		echo >&4
	fi
	(( j = j + 1 ))
done < $1

no=$(wc -l $1 | cut -d " " -f1)
((c=$no-1))
j=0
for (( i=1;i<=n+1;i++ ))
do
	data=$(cut -f$i $1)
	datarr=($data)
	name=${datarr[0]}
	unset datarr[0]
	total=0
	for items in ${datarr[*]}
	do
		(( total = total + items ))
	done
	mac_avg=$(echo "scale=2; $total/$c" | bc)
	IFS=$'\n' sorted=($(sort <<<"${datarr[*]}"))
	unset IFS
	if (( c % 2 == 0 ))
	then
		(( num = $c/2 ))
		(( med = ${sorted[$num]} + ${sorted[$num-1]} ))
		median=$(echo "scale=2; $med/2" | bc)
	else
		(( num = ($c+1)/2 ))
		(( med=${sorted[$num-1]} ))
		median=$(echo "scale=2; $med/1" | bc)
	fi
	if (( $j == 0 ))
	then
		(( j = j+1 ))
	else
		echo "Average temperature for $name was $mac_avg C." >&4
		echo "Median temperature for $name was $median C." >&4
		echo >&4
	fi
done

exit 0

