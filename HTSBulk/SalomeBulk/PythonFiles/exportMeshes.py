# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 11/21/2012


print('*** MED, SAUV, STL and UNV files:')
print(' * assembly.med (MED version 40, other options 30, 12)')
#assemblyMesh.ExportMED(folderDict['med']+'assembly.med', auto_groups = 0, minor = 40, overwrite = 1, meshPart = None, autoDimension = 1)
assemblyMesh.ExportMED(folderDict['med']+'assembly.med', 1, 40, 1, None, 1, [], 'efsv', -1)
#print(' * assembly.sauv')
#assemblyMesh.ExportSAUV(folderDict['sauv']+'assembly.sauv', auto_groups = 1)
#print(' * assembly.stl')
#assemblyMesh.ExportSTL(folderDict['stl']+'assembly.stl', 0)
print(' * assembly.unv')
assemblyMesh.ExportUNV(folderDict['unv']+'assembly.unv')
#print(' * assembly.cgns')
#assemblyMesh.ExportCGNS(pathDirectoryNameOfCgnsFiles+'assembly.cgns')
# print(' * all sub-meshes')
# for i, value in enumerate(listOfSolidMeshGroups):
#     assemblyMesh.ExportMED(folderDict['med']+listOfSolids[i]+'.med', auto_groups = 0, minor = 40, overwrite = 1, meshPart = value, autoDimension = 1)
#     assemblyMesh.ExportSTL(pathDirectoryNameOfStlFiles+listOfSolids[i]+'.stl', 0, value)
#     assemblyMesh.ExportUNV(folderDict['unv']+listOfSolids[i]+'.unv', value)
#     assemblyMesh.ExportCGNS(pathDirectoryNameOfCgnsFiles+listOfSolids[i]+'.cgns', 1, value)


pass
