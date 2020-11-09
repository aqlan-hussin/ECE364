#! /bin/bash

#---------------------------------------
# $Author: ee364a16 $
# $Date: 2017-08-30 13:01:02 -0400 (Wed, 30 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

cd c-files

for items in *.c
do
	gcc -Wall -Werror $items >& /dev/null
	echo -n "Compiling file $items... "
	ret=$(gcc -Wall -Werror $items 2>&1)
	if [[ $? -ne 0 ]]
	then
		echo "Error: Compilation failed."
	else
		echo "Compilation succeeded."
		./a.out >& ${items%.c}.out
	fi
	
done

exit 0
