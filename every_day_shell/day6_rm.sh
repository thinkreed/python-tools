#!/usr/bin/env zsh

#remove a file in . dir
rm 1.txt

#remove an empty dir in . dir
rm -d test

#force not to prompt when removing a file which the user has no writing access
rm -f 1.txt

#to prompt when removing file
rm -i 1.txt

#remove dir and the files in dir
rm -r test
rm -R test

#before remove, overwrite the file three times, first 0xff, then 0x00, last 0xff
rm -P 1.txt

#undo remove, but this operation only supports the files that are filled whiteouts
rm -W 1.txt