#!/bin/zsh

pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -P 4
