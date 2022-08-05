#!/bin/bash

### Create mesh ###
salome="/opt/SALOME-9.9.0-native-UB20.04-SRC/binsalome"
namef=$(find ./Salome -type f -name "main.py")
echo $namef
pathf=$(readlink -f $namef)
echo $pathf
$salome -t $pathf

### Variables ###
name=$(find ./Salome -type f -name "assembly.unv")
echo $name
cp -v $name .

# ### remove the extension for multiple purposes
filename=$(basename $name | cut -d. -f1)
echo $filename

echo "*** MESH GENRATION FROM *UNV input file ***"
rm -r ./MESH
ElmerGrid 8 2 $filename.unv -out MESH
# -autoclean
# For paralelization
# ElmerGrid 8 2 $filename.unv -out MESH -partdual -metiskway 4
# -autoclean
# To see a mesh in gmsh format
ElmerGrid 2 4 MESH -out mesh.msh
# ElmerGrid 14 2 $filename.msh -out MESH
# -autoclean
