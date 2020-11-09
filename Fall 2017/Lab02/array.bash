#! /bin/bash

# $Author: ee364a16 $
# $Date: 2017-09-05 11:08:18 -0400 (Tue, 05 Sep 2017) $

function array 
{
    # Fill out your answer here.
	Arr=(a.txt b.txt c.txt d.txt e.txt)	
	(( r=$RANDOM % 5 ))
	head -n 9 ${Arr[$r]} | tail -n 3
    	return

}


#
# To test your function, you can call it below like this:
#
#array
#
