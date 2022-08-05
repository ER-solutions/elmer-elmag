#!/bin/bash

# for f in *.txt
# do
# 	[ -f "$f" ] && sed 's/,/ /g' $f > $(basename $f | cut -d. -f1).dat
# done

for fl in *.dat
do
  #sed -i 's/^[ \t]*//g' $fl
	sed -i 's/[[:space:]]\+/ /g' $fl
done
