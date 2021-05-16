#!/bin/bash

echo "*** MESH GENRATION FROM *UNV input file ***"
ElmerGrid 8 2 *.unv -out MESH -autoclean
