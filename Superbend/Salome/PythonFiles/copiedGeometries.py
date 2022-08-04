##############
### SALOME ###
##############

### TITLE: copiedGeometries.py
### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### LABORATORY: Institute of Engineering, Engineering faculty
### DATE (english): 12/17/2013
### Units: SI otherwise indicated

### NB: It is necessary to define vertexes in order to give a proper name to the edges built upon them. Without this necessary step, salome mesher does not recognize the edge as part of the current solid generating issues.


##############
### COPIES ###
##############

for i in range(1, numberOfCopies+1):
  print "copy: ", i
  for j, value in enumerate(listOfTranslatedConductiveSolidsForCopy):
    ### Printing id number and corresponding geometry:
    print listOfConductiveSolidNumbers[len(listForConductionAssembly)]+": "+listOfConductiveSolids[len(listForConductionAssembly)]
    ### Translation:
    tempSolid = geompy.MakeTranslation(value, 0., 0., i*packageThickness)
    ### List of geometries ###
    listForConductionAssembly.append(tempSolid)
    listForRadiationAssembly.append(tempSolid)
    listForConvectionAssembly.append(tempSolid)
    ### Visualization ###
    if isIntermediateSolidViewWanted:
      visualizationID1_tempSolid = geompy.addToStudy(tempSolid, "view"+"{0:03d}".format(j+7+(i-1)*len(listOfTranslatedConductiveSolidsForCopy)))
      gg.createAndDisplayGO(visualizationID1_tempSolid);


pass
