### AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
### UNIVERSITY: UNAM
### DATE (english):  05/12/2021
### Units: SI otherwise indicated


################
### GEOMETRY ###
################

# Tool 1
toolHeight = (len(listOfSolids)-1)*coilThickness+(len(listOfSolids)-2)*coilSeparation
tool001 = geompy.MakeCylinderRH(coilInnerRadius, toolHeight)
tool001 = geompy.MakeTranslation(tool001, 0., 0., -0.5*toolHeight)

### Grouping tools ###
listOfTools = [tool001]
tools = geompy.MakeCompound(listOfTools)


### Visualization ###
if isIntermediateSolidViewWanted:
  visualizationID1_tool = geompy.addToStudy(tools, "viewTool")
  gg.createAndDisplayGO(visualizationID1_tool);


pass
