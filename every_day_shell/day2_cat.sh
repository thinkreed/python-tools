#!/usr/bin/env zsh

#print the file to stdout
cat ../gyy.py

#print the file with line numbers on non-blank lines
cat -b ../gyy.py

#print the file with numbered lines
cat -n ../gyy.py

#print the file with non-printing characters and a $ at line end
cat -e ../gyy.py

#print the file as single space
cat -s ../gyy.py

#print the non-printing characters
cat -t ../gyy.py

#disable output buffering
cat -u ../gyy.py

#print the non-printing characters and use 'M-' to denote the non-ascii characters
cat -v ../gyy.py

#print the files in order to stdout
cat ./day1_pipe.sh ../gyy.py





