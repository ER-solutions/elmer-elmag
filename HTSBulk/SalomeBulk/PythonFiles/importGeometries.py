##############
### SALOME ###
##############

### TITLE: importExternalFiles.py
### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### LABORATORY: Institute of Engineering, Faculty of Engineering
### DATE: 11/21/2011
### Units: SI otherwise indicated

### INTRODUCTION: Importing external geometries.


##############
### IMPORT ###
##############

if listOfExternalFiles:
  if chooseFileExtensions == 'step':
    print " *** STEP files"
    for i, value in enumerate(listOfExternalFiles):
      listOfExternalGeometries.append(geompy.ImportSTEP(pathDirectoryNameOfExternalFiles+value+'.stp'))
      print " * "+value+".stp"
  elif chooseFileExtensions == 'brep':
    print " *** BREP files"
    for i, value in enumerate(listOfExternalFiles):
      listOfExternalGeometries.append(geompy.ImportSTEP(pathDirectoryNameOfExternalFiles+value+'.brep'))
      print " * "+value+".brep"
  elif chooseFileExtensions == 'iges':
    print " *** IGES files"
    for i, value in enumerate(listOfExternalFiles):
      listOfExternalGeometries.append(geompy.ImportSTEP(pathDirectoryNameOfExternalFiles+value+'.iges'))
      print " * "+value+".iges"


pass
