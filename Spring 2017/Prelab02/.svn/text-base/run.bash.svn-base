#! /bin/bash

output=$2

if (( $# != 2 ))
then
	echo "Usage: run.bash <source file> <output file>"
	exit 1
fi

if [[ -e $output ]] 
then
	printf "%s exists. Would you like to delete it? " $2
	read ans
	if [[ $ans == "yes" ]] || [[ $ans == "y" ]]
	then
		rm $2
	else
		printf "Enter a new filename: "
		read output
		if [[ -e $output ]]
		then
			rm -f $output
		fi
	fi
fi

touch $output

if ! gcc $1 -o quick_sim
then
	echo "error: quick_sim could not be compiled"
	exit 2
fi

exec 4> output.txt
exec 5> $2

for (( i=1; i <= 32; i=i*2 ))
do
	for (( j=1; j <= 16; j=j*2 ))
	do
		./quick_sim $i $j a >&4
		./quick_sim $i $j i >&4
	done
done

exec 6< output.txt
while read line <&6
do
	name=$(echo $line | cut -d ":" -f2)
	cache=$(echo $line | cut -d ":" -f4)
	width=$(echo $line | cut -d ":" -f6)
	cpi=$(echo $line | cut -d ":" -f8)
	time=$(echo $line | cut -d ":" -f10)
	echo "$name:$cache:$width:$cpi:$time" >&5
done
fastest=$time

exec 7< $2
while read line <&7
do
	time=$(echo $line | cut -d ":" -f5)
	if (( $time < $fastest ))
	then
		fastest=$time
		name=$(echo $line | cut -d ":" -f1)
		cache=$(echo $line | cut -d ":" -f2)
		width=$(echo $line | cut -d ":" -f3)
	fi
done

echo "Fastest run time achieved by $name with cache size $cache and issue width $width was $fastest"

exit 0
