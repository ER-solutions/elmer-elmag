### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### DATE (english): 05/12/2021


print("*** STEP, BREP, IGES, VTK files:")
print(" * assembly.step")
geompy.ExportSTEP(assembly, pathDirectoryNameOfStepFiles+'assembly.step')
#print(" * assembly.brep")
#geompy.ExportBREP(assembly, pathDirectoryNameOfBrepFiles+'assembly.brep')
#print(" * assembly.iges")
#geompy.ExportIGES(assembly, pathDirectoryNameOfIgesFiles+'assembly.iges')
print(" * assembly.vtk")
geompy.ExportVTK(assembly, pathDirectoryNameOfVtkFiles+'assembly.vtk')
print(" * all sub-geometries")
for i, value in enumerate(listOfSolidGroups):
  geompy.ExportSTEP(value, pathDirectoryNameOfStepFiles+listOfSolids[i]+'.step')
  #geompy.ExportBREP(value, pathDirectoryNameOfBrepFiles+listOfSolids[i]+'.brep')
  #geompy.ExportIGES(value, pathDirectoryNameOfIgesFiles+listOfSolids[i]+'.iges')
  geompy.ExportVTK(value, pathDirectoryNameOfVtkFiles+listOfSolids[i]+'.vtk')


pass
