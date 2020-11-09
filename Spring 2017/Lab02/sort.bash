#! /bin/bash

#---------------------------------------
# $Author: ee364f15 $
# $Date: 2017-01-25 14:34:31 -0500 (Wed, 25 Jan 2017) $
#---------------------------------------

# Do not modify above this line.

while getopts f:o:-: foo
do

    case $foo in

	f) if [[ ! -r $OPTARG ]]
	   then
		echo "Error: Input file $OPTARG is not readable."
		exit 3
	   fi
	   input=$OPTARG
	   
	    ;; #This means break

	o) output=$OPTARG
	    ;;

	-) str=$(echo $OPTARG | cut -d "=" -f1)
	   if [[ $str != "column_number" ]]
	   then
		echo "Invalid option."
		exit 2
	   fi
	   val=$(echo $OPTARG | cut -d "=" -f2)
	   ;;

	# The variable $foo gets set to '?' when an invalid option is supplied.
	\?) echo "Invalid option."
	    exit 2
	    ;;

        # Default case
	*) echo "Default case."
	    ;;

    esac

done

words=$(wc -w $input | cut -d " " -f1)
row=$(wc -l $input | cut -d " " -f1)
n=$(( $words / $row ))
if (( $val < 1 || $val > n ))
then
	echo "Error: Invalid column number."
	exit 4
fi

echo "Sorting rows by column #$val."
sort -n -k$val $input >$output

exit 0
