#! /bin/bash

#---------------------------------------
# $Author: ee364a16 $
# $Date: 2017-08-26 13:52:40 -0400 (Sat, 26 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

if (( $# != 2 ))
then
	echo "Usage: ./game_stats.bash <file> <game>"
	exit 1
fi

if [[ ! -e $1 ]]
then
	echo "Error: $1 does not exist"
	exit 2
fi

totalHours=0
totalStudents=0
highest=0

while read line
do
	sp=$(echo $line | cut -d "," -f2)
	if [[ $sp == $2 ]]
	then
		hours=$(echo $line | cut -d "," -f3)
		if (($totalStudents == 0))
		then
			lowest=$hours
		fi		
		((totalHours=totalHours+hours))
		((totalStudents=totalStudents+1))
		if (($hours >= $highest))
		then
			highest=$hours
			studentHigh=$(echo $line | cut -d "," -f1)
		fi
		if (($hours <= $lowest))
		then
			lowest=$hours
			studentLow=$(echo $line | cut -d "," -f1)
		fi
	fi
done < $1

echo "Total students: $totalStudents"
echo "Total hours spent in a day: $totalHours"
echo "$studentHigh spent the highest amount of time in a day: $highest"
echo "$studentLow spent the least amount of time in a day: $lowest"

exit 0
