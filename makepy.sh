#! /bin/bash

read -p "Enter Chapter: " chapter
read -p "Enter Exercise number: " xnum 

cd ~/Py-Projects/
if [ ! -d "Chapter"$chapter"_EX" ]; then
	mkdir Chapter"$chapter"_EX
fi
cd Chapter"$chapter"_EX
mkdir CH"$chapter"_"$xnum"
cd CH"$chapter"_"$xnum"
echo -ne "#!/usr/bin/env python3\n\ndef main():\n\n\nif __name__ == \"__main__\":\n    main()\n"  > main.py
vim main.py

