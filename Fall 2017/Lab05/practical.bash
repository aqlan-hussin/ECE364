#! /bin/bash

#----------------------------------
# $Author: ee364a16 $
# $Date: 2017-09-26 21:46:18 -0400 (Tue, 26 Sep 2017) $
#----------------------------------

function part_a 
{               
    # Fill out your answer here
	Arr=(a.txt b.txt c.txt d.txt)	
	(( r=$RANDOM % 4 ))
	head -n 5 ${Arr[$r]} | tail -n 3
    return                      
}                               

function part_b
{              
    # Fill out your answer here
	if [[ -f $1 ]]
	then
		echo "$1 is a file name"
	elif [[ -d $1 ]]
	then
		echo "$1 is a directory name"
	else
		echo "$1 is not a file or directory name"
	fi
    return                     
}                              

function part_c
{
    # Fill out your answer here
	i=0
	while read line
	do
		Arr[$i]=$line
		(( i = i + 1 ))
	done < "file.txt"
	j=0
	for items in ${Arr[*]}
	do
		count=0
		for item in ${Arr[*]}
		do
			if [[ $item == $items ]]
			then
				(( count = count + 1 ))
			fi
		done
		#echo $count
		if (( $count < 2 ))
		then
			Uniq[$j]=$items
			(( j = j + 1 ))
		fi
	done
	for items in ${Uniq[*]}
	do
		echo $items
	done
    return
}

function part_d
{
    # Fill out your answer here
	w=$(wc -w "temp.txt")
	l=$(wc -l "temp.txt")
	echo "temp.txt has $w words and $l lines"
    return
}

function part_e
{
    # Fill out your answer here
	./ece364.py >& "output.txt"
    return
}

function part_f
{
    # Fill out your answer here
	tail -n +1 "people.csv" | sort -t "," -k5,5 -k7,7 -k1,1 -k2,2 | tail -n 10
    return
}

function part_g
{
    # Fill out your answer here
	string="multimillionaire"
	IFS='' read -r -a arr <<< "$string"
	unset IFS
	#arr=($string)
	echo ${#arr[*]}
	#for items in ${arr[*]}
	#do
	#	echo $items
	#done
    return
}


function part_h
{
    # Fill out your answer here
	cd src
	for i in *.c
	do		
		if gcc $i >& /dev/null
		then
			echo "$i: success"
		else
			echo "$i: failure"
		fi
	done
	cd ..
    return
}

function part_i
{
    # Fill out your answer here
	count=$(grep "PURDUE" info.txt)
	c=0
	for items in ${count[*]}
	do
		(( c = c + 1 ))
	done
	echo $c
    return
}

function part_j
{
    # Fill out your answer here
    return
}

# To test your function, you can call it below like this:
#
part_i
