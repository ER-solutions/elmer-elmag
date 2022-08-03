##############
### SALOME ###
##############

### TITLE: assembly.py
### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### LABORATORY: Institute of Engineering, Engineering faculty
### DATE: 04/11/2013
### Units: SI otherwise indicated

### INTRODUCTION: Conduction, radiation and convection assembly to treat both physical problems in external solvers. It should be noted that the partition algorithm should be used if solids share surfaces as the interfaces are automatically defined for example to be used in contact modelling.


################
### GEOMETRY ###
################

if isMakePartitionWanted:
  print(" *** Partition ***")
  assembly = geompy.MakePartition(listForAssembly)
else:
  print(" *** Compound ***")
  assembly = geompy.MakeCompound(listForAssembly)

### Glueing faces for meshing
if isMakeGlueFacesWanted:
  assembly = geompy.MakeGlueFaces(assembly, tolerance)


pass
