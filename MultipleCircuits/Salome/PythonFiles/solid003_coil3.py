##############
### SALOME ###
##############

### TITLE: solid003_racetrack1.py
### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### LABORATORY: Institute of Engineering, Engineering faculty
### DATE (english): 08/26/2019
### Units: SI otherwise indicated

### NB: It is necessary to define vertexes in order to give a proper name to the edges built upon them. Without this necessary step, salome mesher does not recognize the edge as part of the current solid generating issues.


################
### SOLID003 ###
################

### Printing id number and corresponding geometry:
print(listOfSolidNumbers[len(listForAssembly)]+": "+listOfSolids[len(listForAssembly)])

### Volume ###
solid003 = geompy.MakeMirrorByPlane(solid001, planeVXVY)

### List of geometries ###
listOfSolid003 = [solid003]

listForAssembly.append(solid003)

### Visualization ###
if isIntermediateSolidViewWanted:
  visualizationID1_solid003 = geompy.addToStudy(solid003, "view003:coil_3")
  gg.createAndDisplayGO(visualizationID1_solid003);

pass
