#! /bin/bash

total=0
i=0

while (( $# != 0 ))
do
	((i=i+1))
	total=$(expr $total + $1)
	shift
done
echo "Sum of the numbers is $total"

exit 0
