### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### DATE (english): 05/12/2021


print("*** MED, SAUV, STL and UNV files:")
print(" * assembly.med (MED version 40, other options 30, 12)")
assemblyMesh.ExportMED( pathDirectoryNameOfMedFiles+'assembly.med', 1, 40, 1, None, 1, [], 'efsv',-1 )
#print(" * assembly.sauv")
#assemblyMesh.ExportSAUV(pathDirectoryNameOfSauvFiles+'assembly.sauv', auto_groups = 1)
#print(" * assembly.stl")
#assemblyMesh.ExportSTL(pathDirectoryNameOfStlFiles+'assembly.stl', 0)
print(" * assembly.unv")
assemblyMesh.ExportUNV(pathDirectoryNameOfUnvFiles+'assembly.unv')
#print(" * assembly.cgns")
#assemblyMesh.ExportCGNS(pathDirectoryNameOfCgnsFiles+'assembly.cgns')
print(" * all sub-meshes")
for i, value in enumerate(listOfSolidMeshGroups):
  assemblyMesh.ExportMED(pathDirectoryNameOfMedFiles+listOfSolids[i]+'.med',  auto_groups = 0,minor = 40,overwrite = 1,meshPart = value, autoDimension = 1)
  #assemblyMesh.ExportSTL(pathDirectoryNameOfStlFiles+listOfSolids[i]+'.stl', 0, value)
  assemblyMesh.ExportUNV(pathDirectoryNameOfUnvFiles+listOfSolids[i]+'.unv', value)
  #assemblyMesh.ExportCGNS(pathDirectoryNameOfCgnsFiles+listOfSolids[i]+'.cgns', 1, value)


pass
