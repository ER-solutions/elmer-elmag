### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### DATE: 05/12/2021


if areMeshGroupsWanted:
  print(" *** Solids: ")
  for i, value in enumerate(listOfSolidGroups):
    listOfSolidMeshGroups.append(assemblyMesh.GroupOnGeom(value, listOfSolidNumbers[i], SMESH.VOLUME))
    print(listOfSolidNumbers[i]+": "+listOfSolids[i])
  print(" *** Faces: ")
  if listOfFaces:
    for i, value in enumerate(listOfFaceGroups):
      listOfFaceMeshGroups.append(assemblyMesh.GroupOnGeom(value, listOfFaceNumbers[i], SMESH.FACE))
      print(listOfFaceNumbers[i]+": "+listOfFaces[i])
  print(" *** Edges: ")
  if listOfEdges:
    for i, value in enumerate(listOfEdgeGroups):
      listOfEdgeMeshGroups.append(assemblyMesh.GroupOnGeom(value, listOfEdgeNumbers[i], SMESH.EDGE))
      print(listOfEdgeNumbers[i]+": "+listOfEdges[i])


pass
