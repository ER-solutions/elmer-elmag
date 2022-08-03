############
### BASH ###
############

### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### PLACE: Instituto de Ingenieria, UNAM
### DATE (English): 01/05/2020

#! /bin/bash

### Variables ###
GMSH="/opt/onelab-Linux64/gmsh"

### Get file name of the *.unv mesh
#name=$(find . -type f -name "*.unv")
name=$(find . -type f -name "*.msh")
### remove the extension for multiple purposes
filename=$(basename $name | cut -d. -f1)

echo " "
echo "*** Conversion mesh: *.unv to *.mesh ***"
#ElmerGrid 8 2 $filename.unv -out MESH --autoclean
ElmerGrid 14 2 $filename.msh -out MESH --autoclean

echo " "
echo "*** Computation solution: ElmerSolver ***"
rm log.txt
#$GMSH gmshGUI.py &
ElmerSolver case.sif
### Save the stdout in log.txt
#ElmerSolver case.sif | tee log.txt
### Server run
#nohup ElmerSolver case.sif > log.txt; tail -f log.txt
#
#echo " "
#echo "*** Postprocessing ***"
