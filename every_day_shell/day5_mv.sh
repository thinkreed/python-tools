#!/usr/bin/env zsh

#rename a file
mv day1_pipe.sh day6

#move a file to dir
mv day1_pipe.sh hello/

#promot in console when mv will overwrite an existing file
mv -i day1_pipe.sh day6

#do not promot when mv will overwrite an existing file
mv -f day1_pipe.sh day6

#do not overwrite an existing file
mv -n day1_pipe.sh day6