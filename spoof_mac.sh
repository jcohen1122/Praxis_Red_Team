#!/bin/bash

NEW_MAC="$1"
cd ~/redteam/bluez/tools
sudo ./bdaddr -i hci0 $NEW_MAC
sudo systemctl daemon-reload
sudo systemctl restart bluetooth
echo "Device reset: new mac active."
