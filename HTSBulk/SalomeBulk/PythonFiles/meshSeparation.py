### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### DATE (english): 11/21/2012


##################
### SEPARATION ###
##################

if isMeshSeparationWanted:
  print " *** Separate meshes for interface modelling:"
  ### Solids:
  if listOfConductiveTranslatedSolids:
    print " * Solids:"
    for i, value in enumerate(listOfConductiveTranslatedSolids):
      print value
      if (listOfTranslationDirection[i] == 'OX'):
        [tempObject001] = conductionMesh.TranslateObject(listOfConductiveSolidMeshGroups[listOfConductiveSolidMeshGroupForTranslation[i]], [listOfTranslationFactors[i]*interfaceDistance, 0., listOfTranslationFactors[0]*interfaceDistance], True, True)
      elif (listOfTranslationDirection[i] == 'OY'):
        [tempObject001] = conductionMesh.TranslateObject(listOfConductiveSolidMeshGroups[listOfConductiveSolidMeshGroupForTranslation[i]], [0., listOfTranslationFactors[i]*interfaceDistance, listOfTranslationFactors[0]*interfaceDistance], True, True)
      else:
        [tempObject001] = conductionMesh.TranslateObject(listOfConductiveSolidMeshGroups[listOfConductiveSolidMeshGroupForTranslation[i]], [0., 0., listOfTranslationFactors[i]*interfaceDistance], True, True)
      smesh.SetName(tempObject001, listOfConductiveTranslatedSolidNumbers[i])
  ### Faces:
  if listOfConductiveTranslatedFaces:
    print " * Faces:"
    print listOfConductiveTranslatedFaces[0]
    [tempObject001] = conductionMesh.TranslateObject(listOfConductiveFaceMeshGroups[1], SMESH.DirStruct(SMESH.PointStruct(0., 0., interfaceDistance)), True, True)
    smesh.SetName(tempObject001, listOfConductiveTranslatedFaceNumbers[0])
  ### Interfaces:
  if listOfTranslatedInterfaces:
    print " * Faces:"
    print listOfTranslatedInterfaces[0]
    [tempObject001] = conductionMesh.TranslateObject(listOfInterfaceMeshGroups[0], SMESH.DirStruct(SMESH.PointStruct(0., 0., interfaceDistance)), True, True)
    smesh.SetName(tempObject001, listOfTranslatedInterfaceNumbers[0])


pass
