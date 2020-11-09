#! /bin/bash

#----------------------------------
# $Author$
# $Date$
#----------------------------------

function part_a 
{               
    # Fill out your answer here
	cd myDir
	files=( *."pdf" )
	echo "Number of pdf files: ${#files[@]}"
	cd ..
    	return                      
}                               

function part_b
{              
    # Fill out your answer here
	n=2
	sed -n "${n}p" < data.txt
    	return                     
}                              

function part_c
{
    # Fill out your answer here
	chmod +x userinput.o
	./userinput.o input.txt
    	return
}

function part_d
{
    # Fill out your answer here
	if cmp -s "foo1.txt" "foo2.txt"
	then
		echo "Files are similar"
	else
		echo "Files are diferent"
	fi
    	return
}

function part_e
{
    # Fill out your answer here
	gcc windows8.c>compile.out
    	return
}

# To test your function, you can call it below like this:
#
part_a
part_b
part_c
part_d
part_e
