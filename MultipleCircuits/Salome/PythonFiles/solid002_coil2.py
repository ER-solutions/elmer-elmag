##############
### SALOME ###
##############

### TITLE: solid002_racetrack1.py
### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### LABORATORY: Institute of Engineering, Engineering faculty
### DATE (english): 08/26/2019
### Units: SI otherwise indicated

### NB: It is necessary to define vertexes in order to give a proper name to the edges built upon them. Without this necessary step, salome mesher does not recognize the edge as part of the current solid generating issues.


################
### SOLID002 ###
################

### Printing id number and corresponding geometry:
print(listOfSolidNumbers[len(listForAssembly)]+": "+listOfSolids[len(listForAssembly)])

### Volume ###
solid002 = geompy.MakeTranslation(solid001, 0., 0., coil2Position_z)

### List of geometries ###
listOfSolid002 = [solid002]

listForAssembly.append(solid002)

### Visualization ###
if isIntermediateSolidViewWanted:
  visualizationID1_solid002 = geompy.addToStudy(solid002, "view002:coil_2")
  gg.createAndDisplayGO(visualizationID1_solid002);

pass
