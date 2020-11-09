#! /bin/bash

#---------------------------------------
# $Author: ee364a16 $
# $Date: 2017-08-29 11:14:28 -0400 (Tue, 29 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

if (( $# != 1 ))
then
	echo "Usage: ./check_permissions.bash <input file/directory>"
	exit 1
fi

if [[ -f $1 ]]
then
	echo "$1 is an ordinary file"
	perm=$(ls -l $1 | cut -d " " -f1)
elif [[ -d $1 ]]
then
	echo "$1 is a directory"
	perm=$(ls -ld $1 | cut -d " " -f1)
else
	echo "$1 is neither an ordinary file nor a directory"
fi

#perm=$(ls -l $1 | cut -d " " -f1)

for ((i=1;i<=10;i++))
do
	arr[$i]=$(echo $perm | cut -c $i)
done

echo

echo "Owner Permissions:"

if [[ ${arr[2]} == "r" ]]
then
	echo "$1 is readable"
else
	echo "$1 is not readable"
fi
if [[ ${arr[3]} == "w" ]]
then
	echo "$1 is writable"
else
	echo "$1 is not writable"
fi
if [[ ${arr[4]} == "x" ]]
then
	echo "$1 is executable"
else
	echo "$1 is not executable"
fi

echo

echo "Group Permissions:"

if [[ ${arr[5]} == "r" ]]
then
	echo "$1 is readable"
else
	echo "$1 is not readable"
fi
if [[ ${arr[6]} == "w" ]]
then
	echo "$1 is writable"
else
	echo "$1 is not writable"
fi
if [[ ${arr[7]} == "x" ]]
then
	echo "$1 is executable"
else
	echo "$1 is not executable"
fi

echo

echo "Others Permissions:"

if [[ ${arr[8]} == "r" ]]
then
	echo "$1 is readable"
else
	echo "$1 is not readable"
fi
if [[ ${arr[9]} == "w" ]]
then
	echo "$1 is writable"
else
	echo "$1 is not writable"
fi
if [[ ${arr[10]} == "x" ]]
then
	echo "$1 is executable"
else
	echo "$1 is not executable"
fi

echo

exit 0
