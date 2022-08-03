### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### DATE (english): 11/29/2012


### Solids ###
if areSolidGroupsWanted:
  print(" *** Solids: ")
  for i in range(0, len(listOfSolids)):
    listOfSolidGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType["SOLID"]))
  ### SOL001: coil 1
  listOfTemporarySolidIDs = [2]
  for j, v in enumerate(listOfTemporarySolidIDs):
    geompy.AddObject(listOfSolidGroups[0], v)
  print(listOfSolidNumbers[0]+": "+listOfSolids[0])
  ### SOL002: coil 2
  listOfTemporarySolidIDs = [24]
  for j, v in enumerate(listOfTemporarySolidIDs):
    geompy.AddObject(listOfSolidGroups[1], v)
  print(listOfSolidNumbers[1]+": "+listOfSolids[1])
  ### SOL003: coil 3
  listOfTemporarySolidIDs = [46]
  for j, v in enumerate(listOfTemporarySolidIDs):
    geompy.AddObject(listOfSolidGroups[2], v)
  print(listOfSolidNumbers[2]+": "+listOfSolids[2])
  ### SOL005: core
  listOfTemporarySolidIDs = [68]
  for j, v in enumerate(listOfTemporarySolidIDs):
    geompy.AddObject(listOfSolidGroups[3], v)
  print(listOfSolidNumbers[3]+": "+listOfSolids[3])
  ### SOL005: air
  listOfTemporarySolidIDs = [93]
  for j, v in enumerate(listOfTemporarySolidIDs):
    geompy.AddObject(listOfSolidGroups[4], v)
  print(listOfSolidNumbers[4]+": "+listOfSolids[4])


### Faces ###
if areFaceGroupsWanted:
  print(" *** Faces:")
  ### Conduction (for boundary conditions) ###
  if listOfFaces:
    for i in range(0, len(listOfFaces)):
      listOfFaceGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType["FACE"]))
    ### FAC001: coil 1
    for j in range(len(listOfSolidGroups[0:3])):
        listOfTemporaryFaceIDs = geompy.ExtractShapes(listOfSolidGroups[j], geompy.ShapeType["SHELL"], True)
        geompy.UnionList(listOfFaceGroups[j], listOfTemporaryFaceIDs)
        geompy.addToStudyInFather(assembly, listOfFaceGroups[j], 'coil'+str(j)+'Boundary' )
        print(listOfFaceNumbers[j]+": "+listOfFaces[j])
    ### FAC002: air boundary
    listOfTemporaryFaceIDs_air = [95]
    for j, v in enumerate(listOfTemporaryFaceIDs_air):
      geompy.AddObject(listOfFaceGroups[3], v)
    print(listOfFaceNumbers[3]+": "+listOfFaces[3])


### Edges ###
if areEdgeGroupsWanted:
  print(" *** Edges:")
  ### Conduction (for boundary conditions) ###
  if listOfEdges:
    for i in range(0, len(listOfEdges)):
      listOfEdgeGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType["EDGE"]))
    ### EDG001: axis
    listOfTemporaryEdgeIDs_axis = [90]
    for j, v in enumerate(listOfTemporaryEdgeIDs_axis):
      geompy.AddObject(listOfEdgeGroups[0], v)
    print(listOfEdgeNumbers[0]+": "+listOfEdges[0])


if areSubmeshGroupsWanted:
  ### SUBMESH of solids and faces ...###
  print(" *** Submeshed solids: coils and iron")
  submeshSolidGroup = geompy.CreateGroup(assembly, geompy.ShapeType["SOLID"])
  geompy.UnionList(submeshSolidGroup, listOfSolidGroups[0:3])
  print(" *** Submeshed faces: air boundary")
  submeshFaceGroup = geompy.CreateGroup(assembly, geompy.ShapeType["FACE"])
  for j, v in enumerate(listOfTemporaryFaceIDs_air):
    geompy.AddObject(submeshFaceGroup, v)
  print(" *** Submeshed edges: axis")
  submeshEdgeGroup = geompy.CreateGroup(assembly, geompy.ShapeType["EDGE"])
  for j, v in enumerate(listOfTemporaryEdgeIDs_axis):
    geompy.AddObject(submeshEdgeGroup, v)

pass
