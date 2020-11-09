#! /bin/bash

#---------------------------------------
# $Author: ee364a16 $
# $Date: 2017-08-29 11:14:28 -0400 (Tue, 29 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

if (( $# != 1 )) || (( $1 < 0 ))
then
	echo "Usage: ./kaprekar.bash <non-negative integer>"
	exit 1
fi

y=1

for (( i=1; i<=$1; i++ ))
do
	sq=$((i*i))
	n=${#sq}
	
	if (( $n == 1 ))
	then
		num[1]=$(echo $sq | cut -c 1)
		num[2]=0
	elif (( $n % 2 == 0 ))
	then
		x=$((n/2))		
		num[1]=$(echo $sq | cut -c 1-$x)
		x=$((n/2+1))
		num[2]=$(echo $sq | cut -c $x-$n)		
	else
		x=$(( (n-1)/2 ))		
		num[1]=$(echo $sq | cut -c 1-$x)
		x=$(( (n-1)/2+1 ))
		num[2]=$(echo $sq | cut -c $x-$n)
	fi
	c=${num[2]}
	kap=${num[1]}+$((10#$c))
	if (($kap == $i))
	then
		kaparr[$y]=$i
		sqarr[$y]=$sq
		n1[$y]=${num[1]}
		n2[$y]=${num[2]}
		y=$((y+1))
	fi
done

for (( index=1;index<=$((y-1));index++ ))
do
	echo "${kaparr[$index]}, square=${sqarr[$index]}. ${n1[$index]}+${n2[$index]}=${kaparr[$index]}"
done 

exit 0
