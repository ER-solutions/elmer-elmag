##############
### SALOME ###
##############

### TITLE: solid004_racetrack1.py
### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### LABORATORY: Institute of Engineering, Engineering faculty
### DATE (english): 08/26/2019
### Units: SI otherwise indicated

### NB: It is necessary to define vertexes in order to give a proper name to the edges built upon them. Without this necessary step, salome mesher does not recognize the edge as part of the current solid generating issues.


################
### SOLID004 ###
################

### Printing id number and corresponding geometry:
print(listOfSolidNumbers[len(listForAssembly)]+": "+listOfSolids[len(listForAssembly)])

# vertexes
vertex001 = geompy.MakeVertex(0., 0., corePosition_z)

### Volume ###
solid004 = geompy.MakeCylinder(vertex001, VZ, coreRadius,coreHeight)
solid004 = geompy.MakeCut(solid004, geompy.MakeCompound(listForAssembly))

### List of geometries ###
listOfSolid004 = [solid004]

listForAssembly.append(solid004)

### Visualization ###
if isIntermediateSolidViewWanted:
  visualizationID1_solid004 = geompy.addToStudy(solid004, "view004:core")
  gg.createAndDisplayGO(visualizationID1_solid004);

pass
