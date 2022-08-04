#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.7.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/ftrillaudp/GitHub/HTS-bulks/Onelab/BulkWithDefects/Salome-Bulk/PythonFiles')

####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("scaling", 0.001)
notebook.set("bulk1Radius", 0.015)
notebook.set("bulk1Height", 0.015)
notebook.set("airRadius", 0.03)
notebook.set("airHeight", 0.03)
####################################################
##        End of NoteBook variables section       ##
####################################################
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

geomObj_1 = geompy.MakeVertex(0, 0, 0)
geomObj_2 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_3 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_4 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_5 = geompy.MakePlane2Vec(geomObj_2, geomObj_3, 1)
geomObj_6 = geompy.MakePlane2Vec(geomObj_3, geomObj_2, 1)
geomObj_7 = geompy.MakePlane2Vec(geomObj_2, geomObj_4, 1)
geomObj_8 = geompy.MakeCompound([geomObj_7, geomObj_5, geomObj_6])
geomObj_9 = geompy.MakeCylinderRH(0.015, 0.015)
geomObj_10 = geompy.MakeTranslation(geomObj_9, 0, 0, -0.0075)
geomObj_11 = geompy.MakeVertex(0, 0, -0.0165)
geomObj_12 = geompy.MakeVertex(0, 0, 0.0165)
geomObj_13 = geompy.MakeEdge(geomObj_11, geomObj_12)
geomObj_14 = geompy.MakeCylinderRH(0.03, 0.03)
geomObj_15 = geompy.MakeTranslation(geomObj_14, 0, 0, -0.015)
geomObj_16 = geompy.MakeCompound([geomObj_10])
geomObj_17 = geompy.MakeCut(geomObj_15, geomObj_16)
geomObj_18 = geompy.MakePartition([geomObj_10, geomObj_17, geomObj_13], [], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
geomObj_19 = geompy.MakeGlueFaces(geomObj_18, 1e-06)
geomObj_20 = geompy.MakeCDG(geomObj_10)
geomObj_21 = geompy.MakeCDG(geomObj_17)
geomObj_22 = geompy.CreateGroup(geomObj_19, geompy.ShapeType["SOLID"])
geompy.AddObject(geomObj_22, 2)
[geomObj_23] = geompy.ExtractShapes(geomObj_22, geompy.ShapeType["SHELL"], True)
geomObj_24 = geompy.CreateGroup(geomObj_19, geompy.ShapeType["SOLID"])
geompy.AddObject(geomObj_24, 18)
[geomObj_25,geomObj_26] = geompy.ExtractShapes(geomObj_24, geompy.ShapeType["SHELL"], True)
geomObj_27 = geompy.CreateGroup(geomObj_19, geompy.ShapeType["FACE"])
geomObj_28 = geompy.CreateGroup(geomObj_19, geompy.ShapeType["FACE"])
geompy.UnionList(geomObj_27, [geomObj_23])
geomObj_29 = geompy.MakeVertex(0, 0, 0)
geomObj_30 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_31 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_32 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_33 = geompy.MakePlane2Vec(geomObj_30, geomObj_31, 1)
geomObj_34 = geompy.MakePlane2Vec(geomObj_31, geomObj_30, 1)
geomObj_35 = geompy.MakePlane2Vec(geomObj_30, geomObj_32, 1)
geomObj_36 = geompy.MakeCompound([geomObj_35, geomObj_33, geomObj_34])
geomObj_37 = geompy.MakeCylinderRH(0.015, 0.015)
geomObj_38 = geompy.MakeTranslation(geomObj_37, 0, 0, -0.0075)
geomObj_39 = geompy.MakeVertex(0, 0, -0.0165)
geomObj_40 = geompy.MakeVertex(0, 0, 0.0165)
geomObj_41 = geompy.MakeEdge(geomObj_39, geomObj_40)
geomObj_42 = geompy.MakeCylinderRH(0.03, 0.03)
geomObj_43 = geompy.MakeTranslation(geomObj_42, 0, 0, -0.015)
geomObj_44 = geompy.MakeCompound([geomObj_38])
geomObj_45 = geompy.MakeCut(geomObj_43, geomObj_44)
geomObj_46 = geompy.MakePartition([geomObj_38, geomObj_45, geomObj_41], [], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
geomObj_47 = geompy.MakeGlueFaces(geomObj_46, 1e-06)
geomObj_48 = geompy.MakeCDG(geomObj_38)
geomObj_49 = geompy.MakeCDG(geomObj_45)
geomObj_50 = geompy.CreateGroup(geomObj_47, geompy.ShapeType["SOLID"])
geompy.AddObject(geomObj_50, 2)
[geomObj_51] = geompy.ExtractShapes(geomObj_50, geompy.ShapeType["SHELL"], True)
geomObj_52 = geompy.CreateGroup(geomObj_47, geompy.ShapeType["SOLID"])
geompy.AddObject(geomObj_52, 18)
[geomObj_53,geomObj_54] = geompy.ExtractShapes(geomObj_52, geompy.ShapeType["SHELL"], True)
[geomObj_55,geomObj_56] = geompy.ExtractShapes(geomObj_52, geompy.ShapeType["SHELL"], True)
[geomObj_57,geomObj_58] = geompy.ExtractShapes(geomObj_52, geompy.ShapeType["SHELL"], True)
geomObj_59 = geompy.CreateGroup(geomObj_47, geompy.ShapeType["FACE"])
geomObj_60 = geompy.CreateGroup(geomObj_47, geompy.ShapeType["FACE"])
geompy.UnionList(geomObj_59, [geomObj_51])
geomObj_61 = geompy.MakeVertex(0, 0, 0)
VX = geompy.MakeVectorDXDYDZ(1, 0, 0)
VY = geompy.MakeVectorDXDYDZ(0, 1, 0)
VZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
planeOXZ = geompy.MakePlane2Vec(VX, VY, 1)
planeOYZ = geompy.MakePlane2Vec(VY, VX, 1)
planeOXY = geompy.MakePlane2Vec(VX, VZ, 1)
PlanesOXYZ = geompy.MakeCompound([planeOXY, planeOXZ, planeOYZ])
geomObj_62 = geompy.MakeCylinderRH(0.015, 0.015)
geomObj_63 = geompy.MakeTranslation(geomObj_62, 0, 0, -0.0075)
geomObj_64 = geompy.MakeVertex(0, 0, -0.0165)
geomObj_65 = geompy.MakeVertex(0, 0, 0.0165)
geomObj_66 = geompy.MakeEdge(geomObj_64, geomObj_65)
geomObj_67 = geompy.MakeCylinderRH(0.03, 0.03)
geomObj_68 = geompy.MakeTranslation(geomObj_67, 0, 0, -0.015)
geomObj_69 = geompy.MakeCompound([geomObj_63])
geomObj_70 = geompy.MakeCut(geomObj_68, geomObj_69)
geomObj_71 = geompy.MakePartition([geomObj_63, geomObj_70, geomObj_66], [], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
Assembly = geompy.MakeGlueFaces(geomObj_71, 1e-06)
geomObj_72 = geompy.MakeCDG(geomObj_63)
geomObj_73 = geompy.MakeCDG(geomObj_70)
S001__bulk = geompy.CreateGroup(Assembly, geompy.ShapeType["SOLID"])
geompy.AddObject(S001__bulk, 2)
[geomObj_74] = geompy.ExtractShapes(S001__bulk, geompy.ShapeType["SHELL"], True)
S002__air = geompy.CreateGroup(Assembly, geompy.ShapeType["SOLID"])
geompy.AddObject(S002__air, 18)
[geomObj_75,geomObj_76] = geompy.ExtractShapes(S002__air, geompy.ShapeType["SHELL"], True)
F001__bulkBoundary = geompy.CreateGroup(Assembly, geompy.ShapeType["FACE"])
F002__airBoundary = geompy.CreateGroup(Assembly, geompy.ShapeType["FACE"])
geompy.UnionList(F001__bulkBoundary, [geomObj_74])
[geomObj_77,geomObj_78,geomObj_79,geomObj_80] = geompy.SubShapeAll(F001__bulkBoundary, geompy.ShapeType["VERTEX"])
geompy.UnionList(F002__airBoundary, [geomObj_75, geomObj_76])
geomObj_81 = geompy.GetInPlace(Assembly, S001__bulk, True)
[geomObj_82,geomObj_83,geomObj_84,geomObj_85] = geompy.SubShapeAll(geomObj_81, geompy.ShapeType["VERTEX"])
[geomObj_86,geomObj_87,geomObj_88] = geompy.SubShapeAll(geomObj_81, geompy.ShapeType["FACE"])
geomObj_89 = geompy.GetInPlace(Assembly, S001__bulk, True)
[geomObj_90,geomObj_91,geomObj_92] = geompy.SubShapeAll(geomObj_89, geompy.ShapeType["FACE"])
[geomObj_93,geomObj_94,geomObj_95] = geompy.SubShapeAll(geomObj_89, geompy.ShapeType["FACE"])
Group_1 = geompy.CreateGroup(Assembly, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_1, [4, 11, 14])
S001__bulk.SetColor(SALOMEDS.Color(0,0,0))
S002__air.SetColor(SALOMEDS.Color(0,0.3,1))
F001__bulkBoundary.SetColor(SALOMEDS.Color(1,0,0))
F002__airBoundary.SetColor(SALOMEDS.Color(0,0.3,1))
geompy.addToStudyInFather( planeOXY, VX, 'VX' )
geompy.addToStudyInFather( planeOXY, VY, 'VY' )
geompy.addToStudyInFather( planeOXZ, VZ, 'VZ' )
geompy.addToStudyInFather( PlanesOXYZ, planeOXZ, 'planeOXZ' )
geompy.addToStudyInFather( PlanesOXYZ, planeOYZ, 'planeOYZ' )
geompy.addToStudyInFather( PlanesOXYZ, planeOXY, 'planeOXY' )
geompy.addToStudy( PlanesOXYZ, 'PlanesOXYZ' )
geompy.addToStudy( Assembly, 'Assembly' )
geompy.addToStudyInFather( Assembly, S001__bulk, 'S001: bulk' )
geompy.addToStudyInFather( Assembly, S002__air, 'S002: air' )
geompy.addToStudyInFather( Assembly, F001__bulkBoundary, 'F001: bulkBoundary' )
geompy.addToStudyInFather( Assembly, F002__airBoundary, 'F002: airBoundary' )
geompy.addToStudyInFather( Assembly, Group_1, 'Group_1' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()