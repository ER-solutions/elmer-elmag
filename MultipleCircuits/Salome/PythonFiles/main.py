##############
### SALOME ###
##############

### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### DATE (english): 05/12/2021
### Units: SI otherwise indicated


###############
### INCLUDE ###
###############

### Salome:
import salome
import GEOM
import SMESH
from salome.smesh import smeshBuilder
smesh = smeshBuilder.New()
from salome.StdMeshers import StdMeshersBuilder
from salome.geom import geomBuilder
geompy = geomBuilder.New()
import StdMeshers
import NETGENPlugin
import SALOMEDS
import iparameters
import salome_notebook
import MEDLoader
import SALOMEDS

### Python:
import os
import sys
import re
import shutil
import subprocess
import numpy as np
import scipy as sp
import math
from datetime import date


#############
### PATHS ###
#############

basePathDirectoryName = '/home/ftrillaudp/Documents/Codes/Elmerfem/MultipleCircuits/Salome/'
pathDirectoryNameOfPythonFiles = basePathDirectoryName+'PythonFiles/'
pathDirectoryNameOfStepFiles = basePathDirectoryName+'StepFiles/'
pathDirectoryNameOfBrepFiles = basePathDirectoryName+'BrepFiles/'
pathDirectoryNameOfIgesFiles = basePathDirectoryName+'IgesFiles/'
pathDirectoryNameOfVtkFiles = basePathDirectoryName+'VtkFiles/'
pathDirectoryNameOfStlFiles = basePathDirectoryName+'StlFiles/'
pathDirectoryNameOfUnvFiles = basePathDirectoryName+'UnvFiles/'
pathDirectoryNameOfCgnsFiles = basePathDirectoryName+'CgnsFiles/'
pathDirectoryNameOfExternalFiles = basePathDirectoryName+'ExternalFiles/'
pathDirectoryNameOfMedFiles = basePathDirectoryName+'MedFiles/'
pathDirectoryNameOfSauvFiles = basePathDirectoryName+'SauvFiles/'
pathDirectoryNameOfHdfFiles = basePathDirectoryName+'HdfFiles/'
pathDirectoryNameOfDataFiles = basePathDirectoryName+'DataFiles/'
os.chdir(pathDirectoryNameOfPythonFiles)

GlobalFileName = 'coils-geomesh'


##################
### OCC Viewer ###
##################

### Initialize Salome ###
salome.salome_init(0)
### Initialization of the tree view ###
gg = salome.ImportComponentGUI("GEOM")
### Visual parameters ###
ipar = iparameters.IParameters(salome.myStudy.GetCommonParameters("Interface Applicative", 1), True)

### Visual properties ###
### VTKViewer:
ipar.setProperty("AP_ACTIVE_VIEW", "VTKViewer_0_0")
ipar.append("AP_MODULES_LIST", "Mesh")
### OCC viewer:
ipar.setProperty("AP_ACTIVE_VIEW", "OCCViewer_0_0")
ipar.setProperty("AP_ACTIVE_MODULE", "Geometry")
### State of the GUI interface:
ipar.setProperty("AP_SAVEPOINT_NAME", "State: 1")

### Upload salome profile ###
#if salome.sg.hasDesktop():
  #salome.sg.updateObjBrowser(True)
  #iparameters.getSession().restoreVisualState()


#############
### FILES ###
#############

### USER DEFINED RUNS ###
### Using tools:
runTools = 1
### Create the various geometries:
runGeometries = 1
### Assemble the geometries:
runAssembly = 1
### VIsualization of the geometries:
runVisualization = 1
### Meshing the geometries:
runMeshing = 1

### MAIN ###
print(" ")
print("### Initialization of parameters ###")
exec(open(pathDirectoryNameOfPythonFiles+"parameters.py").read())
print("### Automatic data ###")
exec(open(pathDirectoryNameOfPythonFiles+"automatic.py").read())
print(" ")

if runTools:
  print("### Tools ###")
  exec(open(pathDirectoryNameOfPythonFiles+"tools.py").read())
  print(" ")

if runGeometries:
  print("### Geometrical models ###")
  for i, value in enumerate(listOfSolids):
    exec(open(pathDirectoryNameOfPythonFiles+"solid"+"{0:03d}".format(i+1)+"_"+value+".py").read())
  print(" ")

if runAssembly:
  exec(open(pathDirectoryNameOfPythonFiles+"assembly.py").read()) # Only if more than one geometry
  exec(open(pathDirectoryNameOfPythonFiles+"properties.py").read())
  print(" ")

if runVisualization:
  print("### Geometrical groups ###")
  exec(open(pathDirectoryNameOfPythonFiles+"geometricGroups.py").read())
  print("### Visualization ###")
  exec(open(pathDirectoryNameOfPythonFiles+"printing.py").read())
  print("### Exporting Geometrical models ###")
  exec(open(pathDirectoryNameOfPythonFiles+"exportGeometries.py").read())
  print(" ")

if runMeshing:
  print("### Meshes ###")
  exec(open(pathDirectoryNameOfPythonFiles+"meshes.py").read())
  print("### Mesh groups ###")
  exec(open(pathDirectoryNameOfPythonFiles+"meshGroups.py").read())
  print("### Exporting mesh files ###")
  exec(open(pathDirectoryNameOfPythonFiles+"exportMeshes.py").read())
  print(" ")


############
### SAVE ###
############

currentStudy = salome.myStudy
salome.myStudy.SaveAs(pathDirectoryNameOfHdfFiles+GlobalFileName+'.hdf', currentStudy, False)
geompy.init_geom()


pass
