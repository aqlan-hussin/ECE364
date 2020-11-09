#! /bin/bash

#---------------------------------------
# $Author: ee364a16 $
# $Date: 2017-08-26 13:52:40 -0400 (Sat, 26 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

q=0
while (( $q != 1 ))
do
	read -p "Enter a command: " com	
	if [[ $com == "hello" ]]
	then
		echo "Hello $(whoami)"
	elif [[ $com == "quit" ]]
	then
		echo "Goodbye"
		q=1
	elif [[ $com == "compile" ]]
	then
		for i in *.c
		do		
			if gcc -Wall -Werror $i -o ${i%.c}.o
			then
				echo "Compilation succeeded for: $i"
			else
				echo "Compilation failed for: $i"
			fi
		done
	elif [[ $com == "whereami" ]]
	then
		echo $PWD
	else
		echo "Error: unrecognized input"
	fi
done

exit 0
