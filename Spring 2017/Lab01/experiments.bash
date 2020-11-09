#! /bin/bash

#---------------------------------------
# $Author: ee364f15 $
# $Date: 2017-01-18 14:08:11 -0500 (Wed, 18 Jan 2017) $
#---------------------------------------

# Do not modify above this line.

i=0

if (( $# == 0 ))
then
	echo "Usage: experimets.bash <input 1> [input 2] .. [input N]"
	exit 1
fi

while (( $# != 0 ))
do
	((i=i+1))
	echo "$1:"
	if [[ ! -r $1 ]]
	then		
		echo "Filename \"$1\" is not readable."
	else
		while read line
		do
			j=1
			total=0
			avg=0		
			for word in $line
			do
				if (( j == 1 ))
				then
					printf "%s " $word
				else
					let total=total+$word
					if (( j == 4 ))
					then
						let avg=total/3
						printf "%d %d\n" $total $avg
					fi			
				fi
				let j=j+1
			done
		done < $1
	fi
	printf "\n"	
	shift
done

exit 0