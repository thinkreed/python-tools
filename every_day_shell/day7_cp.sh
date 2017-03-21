#!/usr/bin/env zsh

#cp the content from src to des
cp src.txt dst.txt

#Preserves structure and attributes of files but not directory structure
cp -a robot/ robot2/

#cp the dir and entire subtree to dst
cp -R robot robot2