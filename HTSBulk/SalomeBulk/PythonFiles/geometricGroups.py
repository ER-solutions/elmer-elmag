# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 11/29/2012


# Solids #
if areSolidGroupsWanted:
    print(' *** Solids: ')
    for i in range(0, len(listOfSolids)):
        listOfSolidGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType['SOLID']))
    # SOL001: bulk
    k = 0
    listOfTemporarySolidIDs = [2]
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])
    # SOL002: air
    k = k+1
    listOfTemporarySolidIDs = [18]
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])


# Faces #
if areFaceGroupsWanted:
    print(' *** Faces:')
    # Conduction (for boundary conditions)
    if listOfFaces:
        for i in range(0, len(listOfFaces)):
            listOfFaceGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType['FACE']))
        for i in range(0, numberOfSubmeshToBeRefined):
        # FAC00x: coils
            listOfTemporaryFaceIDs = geompy.ExtractShapes(listOfSolidGroups[i], geompy.ShapeType['SHELL'], True)
            geompy.UnionList(listOfFaceGroups[i], listOfTemporaryFaceIDs)
            geompy.addToStudyInFather(assembly, listOfFaceGroups[i], list(faceDict.keys())[i])
            print(listOfFaceNumbers[i]+': '+listOfFaces[i])
        # FAC020: air boundary
        k = numberOfSubmeshToBeRefined
        listOfTemporaryFaceIDs_air = [20,27,30]
        for j, v in enumerate(listOfTemporaryFaceIDs_air):
            geompy.AddObject(listOfFaceGroups[k], v)
        print(listOfFaceNumbers[k]+': '+listOfFaces[k])


# Edges #
if areEdgeGroupsWanted:
    print(' *** Edges:')
    # Conduction (for boundary conditions)
    if listOfEdges:
        for i in range(0, len(listOfEdges)):
            listOfEdgeGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType['EDGE']))
    # EDG001: axis
    k = 0
    listOfTemporaryEdgeIDs_axis = [17,28,30]
    for j, v in enumerate(listOfTemporaryEdgeIDs_axis):
        geompy.AddObject(listOfEdgeGroups[k], v)
    print(listOfEdgeNumbers[k]+': '+listOfEdges[k])


# SUBMESH of solids and faces ...#
if areSubmeshGroupsWanted:
    print(' *** Submeshed solids: coils')
    submeshSolidGroup = geompy.CreateGroup(assembly, geompy.ShapeType['SOLID'])
    geompy.UnionList(submeshSolidGroup, listOfSolidGroups[0:numberOfSubmeshToBeRefined])
    print(' *** Submeshed faces: air boundary')
    submeshFaceGroup = geompy.CreateGroup(assembly, geompy.ShapeType['FACE'])
    for j, v in enumerate(listOfTemporaryFaceIDs_air):
        geompy.AddObject(submeshFaceGroup, v)
    print(' *** Submeshed edges: axis')
    submeshEdgeGroup = geompy.CreateGroup(assembly, geompy.ShapeType['EDGE'])
    for j, v in enumerate(listOfTemporaryEdgeIDs_axis):
        geompy.AddObject(submeshEdgeGroup, v)


pass
