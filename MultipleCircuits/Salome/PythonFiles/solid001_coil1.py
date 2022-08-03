##############
### SALOME ###
##############

### TITLE: solid001_racetrack1.py
### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### LABORATORY: Institute of Engineering, Engineering faculty
### DATE (english): 08/26/2019
### Units: SI otherwise indicated

### NB: It is necessary to define vertexes in order to give a proper name to the edges built upon them. Without this necessary step, salome mesher does not recognize the edge as part of the current solid generating issues.


################
### SOLID001 ###
################

### Printing id number and corresponding geometry:
print(listOfSolidNumbers[0]+": "+listOfSolids[0])

### Volume ###
solid001 = geompy.MakeCylinderRH(coilInnerRadius+coilWidth, coilThickness)
solid001 = geompy.MakeCut(solid001, tool001)
solid001 = geompy.MakeTranslation(solid001, 0., 0., coil1Position_z)

### List of geometries ###
listOfSolid001 = [solid001]

listForAssembly.append(solid001)

### Visualization ###
if isIntermediateSolidViewWanted:
  visualizationID1_solid001 = geompy.addToStudy(solid001, "view001:coil_1")
  gg.createAndDisplayGO(visualizationID1_solid001);

pass
