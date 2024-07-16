#!/bin/bash

while true; do
	echo "Starting up the oven..."

	# Run python script
	sudo python3 write_char.py

	#Check exit status
	if [ $? -eq 0 ]; then
		echo -e "\nCooked to perfection..."
		break
	else
		echo -e "ITS BURNT! Locking in...\n"
	fi
done
