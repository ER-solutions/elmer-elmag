### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>

#! /bin/bash

### Variables ###
name=$(find ./Salome -type f -name "assembly.unv")
echo $name
cp -v $name .

# ### remove the extension for multiple purposes
filename=$(basename $name | cut -d. -f1)
echo $filename

echo " "
echo "*** Conversion mesh: *.unv to *.mesh ***"
rm -r ./MESH
ElmerGrid 8 2 $filename.unv -out MESH --autoclean
# ElmerGrid 8 2 $filename.unv -out MESH -partdual -metiskway 4 --autoclean
# ElmerGrid 14 2 $filename.msh -out MESH --autoclean

# To see a mesh in gmsh format
ElmerGrid 2 4 MESH

echo " "
echo "*** Computation solution: ElmerSolver ***"
# Running in standard ouput and saving log at the same time
ElmerSolver case.sif | tee log.txt
#mpirun -np 4 ElmerSolver case.sif | tee log.txt
#
#echo " "
#echo "*** Postprocessing ***"
