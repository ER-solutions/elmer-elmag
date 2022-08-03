##############
### SALOME ###
##############

### TITLE: solid008_air.py
### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### LABORATORY: Institute of Engineering, Engineering faculty
### DATE (english): 12/09/2013
### Units: SI otherwise indicated

### NB: It is necessary to define vertexes in order to give a proper name to the edges built upon them. Without this necessary step, salome mesher does not recognize the edge as part of the current solid generating issues.


################
### solid005 ###
################

### Printing id number and corresponding geometry:
print(listOfSolidNumbers[len(listForAssembly)]+": "+listOfSolids[len(listForAssembly)])

### Vertexes ###
vertex001 = geompy.MakeVertex(0., 0., -1.25*coil1Position_z)
vertex002 = geompy.MakeVertex(0., 0., 1.25*coil1Position_z)

### Edges ###
edge001 = geompy.MakeEdge(vertex001, vertex002)

### Volume ###
solid005 = geompy.MakeSphereR(airRadius)
solid005 = geompy.MakeCut(solid005, geompy.MakeCompound(listForAssembly))

### List of geometries ###
listOfsolid005 = [solid005, edge001]
listForAssembly.append(solid005)
listForAssembly.append(edge001)

### Visualization ###
if isIntermediateSolidViewWanted:
  visualizationID1_solid005 = geompy.addToStudy(solid005, "view005: air")
  gg.createAndDisplayGO(visualizationID1_solid005);


pass
