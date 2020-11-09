#! /bin/bash

#---------------------------------------
# $Author: ee364f15 $
# $Date: 2017-01-25 13:32:22 -0500 (Wed, 25 Jan 2017) $
#---------------------------------------

# Do not modify above this line.

while getopts a:bc:-: foo
do

    case $foo in

	a) echo "You entered the argument '$OPTARG' for the option '-$foo'"
	    ;; #This means break

	b) echo "You entered the argument '$OPTARG' for the option '-$foo'"
	    ;;

	c) echo "You entered the argument '$OPTARG' for the option '-$foo'"
	    ;;

	-) echo "You entered '$OPTARG'."
	   ;;

	# The variable $foo gets set to '?' when an invalid option is supplied.
	\?) echo "Invalid option."
	    ;;

        # Default case
	*) echo "Default case."
	    ;;

    esac

done

exit 0