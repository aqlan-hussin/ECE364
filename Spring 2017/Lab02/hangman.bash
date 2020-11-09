#! /bin/bash

#---------------------------------------
# $Author: ee364f15 $
# $Date: 2017-01-28 21:03:36 -0500 (Sat, 28 Jan 2017) $
#---------------------------------------

# Do not modify above this line.

if (( $# != 0 ))
then
	echo "Usage ./hangman.bash"
	exit 1
fi

A=("banana" "parsimonious" "sesquipedalian")
(( num=$RANDOM % 3 ))
str=${A[$num]}
length=${#str}
word=$(echo $str | fold -w1)

echo "Your word is $length letters long."

B=()

for (( i=0; i < $length; i++ ))
do
	B[$i]="."
	
done

echo -n "Word is: "
for item in ${B[*]}
do
	echo -n "$item "
done

echo

flag=0

while [[ ${word[@]} != ${B[@]} ]]
do	
	j=0
	match=0	
	echo -n "Make a guess: "
	read letter
	echo
	for items in ${word[*]}
	do		
		if [[ $letter == $items ]]
		then
			B[$j]=$letter
			match=1
		fi
		(( j = j + 1 ))
	done
	if (( $match == 1 ))
	then
		echo -n "Good going! "		
		if [[ ${word[@]} == ${B[@]} ]]
		then
			echo			
			echo "Congratulations! You guessed the word: $str"
		else		
			echo -n "Word is: "
			for k in ${B[*]}
			do
				echo -n "$k "
			done
			echo ""
		fi
	else
		echo -n "Sorry, try again. Word is: "
		for k in ${B[*]}
		do
			echo -n "$k "
		done
		echo ""
	fi
done

exit 0

