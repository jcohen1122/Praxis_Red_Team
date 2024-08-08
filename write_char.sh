#!/bin/bash

while true; do
	echo "Starting..."

	# Run python script
	sudo python3 write_char.py

	#Check exit status
	if [ $? -eq 0 ]; then
		echo -e "\nExecuting..."
		break
	else
		echo -e "Error, trying again...\n"
	fi
done
