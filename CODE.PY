##~ running Plaxis3DInput.exe 20.0.0.119
_initializerectangular SoilContour -12.5 0 12.5 12.5
_setproperties "Title" "" "Company" "only @ ::LAVTeam:: (R)" "Comments" "" "UnitForce" "kN" "UnitLength" "m" "UnitTime" "day" "WaterWeight" 10 "ReferenceTemperature" 293.15 "LiquidSpecificHeatCapacity" 4181.3 "LiquidThermalConductivity" 0.0006 "LiquidLatentHeat" 334000 "LiquidThermalExpansion" 0.00021 "LiquidTemperature" 293.15 "IceSpecificHeatCapacity" 2108 "IceThermalConductivity" 0.00222 "IceThermalExpansion" 5E-5 "VapourSpecificHeatCapacity" 1930 "VapourThermalConductivity" 2.5E-5 "VapourSpecificGasConstant" 461.5 "UseTemperatureDepWaterPropsTable" False "ModelType" "Full" "ElementType" "10-Noded"
initializerectangular SoilContour -12.0 0 12.0 8.0
borehole 0 0
set Borehole_1.Head -20.0
soillayer 20.0
soilmat
setproperties SoilMat_1 "MaterialName" "SoilZone_1" "SoilModel" 4 "drainagetype" 0 "gammaUnsat" 17.0 "gammaSat" 17.0 "cref" 0.1 "phi" 32.0 "psi" 2.0 "K0Determination" 0 "K0Primary" 0.5 "K0Secondary" 0.5 "K0PrimaryIsK0Secondary" True "K0nc" 0.4700807357667951 "TensionCutOff" True "TensileStrength" 0 "E50ref" 60000.0 "EoedRef" 60000.0 "EurRef" 180000.0 "nu" 0.2 "powerm" 0.5 "Rf" 0.875 "M" 1.1566286334055067 "Kfac" 1.6294645412552475 "Gi0ref" 53067.869376415874 "G0ref" 216899.8813478647 "gamma07" 0.0001 "ConsiderGapClosure" False
set Soillayer_1.Soil.Material SoilZone_1
soilmat
setproperties SoilMat_1 "MaterialName" "InterfaceForSoilZone_1" "SoilModel" 4 "drainagetype" 0 "gammaUnsat" 17.0 "gammaSat" 17.0 "cref" 0.1 "phi" 29 "psi" 0 "K0Determination" 0 "K0Primary" 0.5 "K0Secondary" 0.5 "K0PrimaryIsK0Secondary" True "K0nc" 0.515190379753663 "TensionCutOff" True "TensileStrength" 0 "E50ref" 60000.0 "EoedRef" 60000.0 "EurRef" 180000.0 "nu" 0.2 "powerm" 0.5 "Rf" 0.875 "M" 0.9735145171990042 "Kfac" 1.6218820454929583 "Gi0ref" 55480.332010333004 "G0ref" 216899.8813478647 "gamma07" 0.0001 "ConsiderGapClosure" False
platemat
setproperties PlateMat3D_1 "MaterialName" "Plate_0.038" "Elasticity" "Elastic" "d" 0.038 "w" 0 "IsIsotropic" True "E1" 210000000.0 "E2" 210000000.0 "Nu12" 0.3 "G12" 80769230.76923077 "G13" 80769230.76923077 "G23" 80769230.76923077
beammat
setproperties BeamMat_1 "MaterialName" "Beam_0.038" "Elasticity" "Elastic" "BeamType" "Predefined" "PredefinedBeamType" "Massive circular beam" "Diameter" 0.038 "w" 0 "E" 210000.0 "nu" 0.3
gotostructures
tunnel (0 0 0) (1 0 0) (0 0 1)
setproperties Tunnel_1.CrossSection "ShapeType" "Circular" "WholeHalfMode" "Right" "OrientationAxis1X" 0 "OrientationAxis1Y" 1 "OrientationAxis1Z" 0 "OrientationAxis2X" 1 "OrientationAxis2Y" 0 "OrientationAxis2Z" 0 "Offset2" -1.0
set Tunnel_1.CrossSection.Segments[0].ArcProperties.Radius 1.0
plate Tunnel_1.SliceSurfaces[0]
posinterface Tunnel_1.PlaneSurfaces[0]
setproperties Tunnel_1.Trajectory "OrientationAxis1X" 0 "OrientationAxis1Y" 0 "OrientationAxis1Z" -1
add Tunnel_1.Trajectory
set Tunnel_1.Trajectory.Segments[0].LineProperties.Length 10.6
generatetunnel Tunnel_1
decouplefromgenerator Volume_1 Surface_2 Surface_1
delete Volume_1 Surface_2 Surface_1
tunnel (0 0 0) (1 0 0) (0 0 1)
setproperties Tunnel_2.CrossSection "ShapeType" "Free" "WholeHalfMode" "Right" "OrientationAxis1X" 0 "OrientationAxis1Y" 1 "OrientationAxis1Z" 0 "OrientationAxis2X" 1 "OrientationAxis2Y" 0 "OrientationAxis2Z" 0 "Offset2" -1.0
add Tunnel_2.CrossSection
set Tunnel_2.CrossSection.Segments[0].SegmentType "Arc"
set Tunnel_2.CrossSection.Segments[0].ArcProperties.CentralAngle 20.0
set Tunnel_2.CrossSection.Segments[0].ArcProperties.Radius 1.0
plate Tunnel_2.SliceSurfaces[0] "Material" Plate_0038
neginterface Tunnel_2.SliceSurfaces[0] "MaterialMode" "From adjacent soil"
add Tunnel_2.CrossSection
set Tunnel_2.CrossSection.Segments[1].SegmentType "Arc"
set Tunnel_2.CrossSection.Segments[1].ArcProperties.CentralAngle 20.0
set Tunnel_2.CrossSection.Segments[1].ArcProperties.Radius 1.0
plate Tunnel_2.SliceSurfaces[0] "Material" Plate_0038
neginterface Tunnel_2.SliceSurfaces[0] "MaterialMode" "From adjacent soil"
add Tunnel_2.CrossSection
set Tunnel_2.CrossSection.Segments[2].SegmentType "Arc"
set Tunnel_2.CrossSection.Segments[2].ArcProperties.CentralAngle 20.0
set Tunnel_2.CrossSection.Segments[2].ArcProperties.Radius 1.0
plate Tunnel_2.SliceSurfaces[0] "Material" Plate_0038
neginterface Tunnel_2.SliceSurfaces[0] "MaterialMode" "From adjacent soil"
add Tunnel_2.CrossSection
set Tunnel_2.CrossSection.Segments[3].SegmentType "Arc"
set Tunnel_2.CrossSection.Segments[3].ArcProperties.CentralAngle 20.0
set Tunnel_2.CrossSection.Segments[3].ArcProperties.Radius 1.0
plate Tunnel_2.SliceSurfaces[0] "Material" Plate_0038
neginterface Tunnel_2.SliceSurfaces[0] "MaterialMode" "From adjacent soil"
add Tunnel_2.CrossSection
set Tunnel_2.CrossSection.Segments[4].SegmentType "Arc"
set Tunnel_2.CrossSection.Segments[4].ArcProperties.CentralAngle 20.0
set Tunnel_2.CrossSection.Segments[4].ArcProperties.Radius 1.0
plate Tunnel_2.SliceSurfaces[0] "Material" Plate_0038
neginterface Tunnel_2.SliceSurfaces[0] "MaterialMode" "From adjacent soil"
add Tunnel_2.CrossSection
set Tunnel_2.CrossSection.Segments[5].SegmentType "Arc"
set Tunnel_2.CrossSection.Segments[5].ArcProperties.CentralAngle 20.0
set Tunnel_2.CrossSection.Segments[5].ArcProperties.Radius 1.0
plate Tunnel_2.SliceSurfaces[0] "Material" Plate_0038
neginterface Tunnel_2.SliceSurfaces[0] "MaterialMode" "From adjacent soil"
add Tunnel_2.CrossSection
set Tunnel_2.CrossSection.Segments[6].SegmentType "Arc"
set Tunnel_2.CrossSection.Segments[6].ArcProperties.CentralAngle 20.0
set Tunnel_2.CrossSection.Segments[6].ArcProperties.Radius 1.0
plate Tunnel_2.SliceSurfaces[0] "Material" Plate_0038
neginterface Tunnel_2.SliceSurfaces[0] "MaterialMode" "From adjacent soil"
add Tunnel_2.CrossSection
set Tunnel_2.CrossSection.Segments[7].SegmentType "Arc"
set Tunnel_2.CrossSection.Segments[7].ArcProperties.CentralAngle 20.0
set Tunnel_2.CrossSection.Segments[7].ArcProperties.Radius 1.0
plate Tunnel_2.SliceSurfaces[0] "Material" Plate_0038
neginterface Tunnel_2.SliceSurfaces[0] "MaterialMode" "From adjacent soil"
add Tunnel_2.CrossSection
set Tunnel_2.CrossSection.Segments[8].SegmentType "Arc"
set Tunnel_2.CrossSection.Segments[8].ArcProperties.CentralAngle 20.0
set Tunnel_2.CrossSection.Segments[8].ArcProperties.Radius 1.0
plate Tunnel_2.SliceSurfaces[0] "Material" Plate_0038
neginterface Tunnel_2.SliceSurfaces[0] "MaterialMode" "From adjacent soil"
setproperties Tunnel_2.Trajectory "OrientationAxis1X" 0 "OrientationAxis1Y" 0 "OrientationAxis1Z" -1
add Tunnel_2.Trajectory
set Tunnel_2.Trajectory.Segments[0].LineProperties.Length 10.6
set Tunnel_2.Slicing[0].SlicingMethod "Number"
set Tunnel_2.Slicing[0].NumberOfSlices 11
generatetunnel Tunnel_2
tunnel (0 0 0) (1 0 0) (0 0 1)
setproperties Tunnel_3.CrossSection "ShapeType" "Circular" "WholeHalfMode" "Right" "OrientationAxis1X" 0 "OrientationAxis1Y" 1 "OrientationAxis1Z" 0 "OrientationAxis2X" 1 "OrientationAxis2Y" 0 "OrientationAxis2Z" 0 "Offset2" -1.4
set Tunnel_3.CrossSection.Segments[0].ArcProperties.Radius 1.4
setproperties Tunnel_3.Trajectory "OrientationAxis1X" 0 "OrientationAxis1Y" 0 "OrientationAxis1Z" -1
add Tunnel_3.Trajectory
set Tunnel_3.Trajectory.Segments[0].LineProperties.Length 10.9
generatetunnel Tunnel_3
tunnel (0 0 10.0) (-1 0 0) (0 0 1)
setproperties Tunnel_4.CrossSection "ShapeType" "Circular" "WholeHalfMode" "Right" "OrientationAxis1X" 0 "OrientationAxis1Y" 1 "OrientationAxis1Z" 0 "OrientationAxis2X" 1 "OrientationAxis2Y" 0 "OrientationAxis2Z" 0 "Offset2" -1.0
set Tunnel_4.CrossSection.Segments[0].ArcProperties.Radius 1.0
plate Tunnel_4.SliceSurfaces[0] "Material" Plate_0038
plate Tunnel_4.PlaneSurfaces[0] "Material" Plate_0038
rigidbody Tunnel_4.PlaneSurfaces[0]
setproperties Tunnel_4.PlaneSurfaces[0].RigidBody "Zref" 10.0
setproperties Tunnel_4.Trajectory "OrientationAxis1X" 0 "OrientationAxis1Y" 0 "OrientationAxis1Z" -1
add Tunnel_4.Trajectory
set Tunnel_4.Trajectory.Segments[0].LineProperties.Length 10.0
set Tunnel_4.Slicing[0].SlicingMethod "Number"
set Tunnel_4.Slicing[0].NumberOfSlices 1
generatetunnel Tunnel_4
decouplefromgenerator Volume_13 Surface_103
delete Surface_103 Volume_13
line (-1.0 0 10.0) (-1.0 0 -10.6)
line (1.0 0 10.0) (1.0 0 -10.6)
beam (Line_1 Line_2) "Material" Beam_0038
gotostages
activate Soils InitialPhase
phase InitialPhase
setproperties Phase_1 "Identification" "Pile wished in place"
activate Plates Phase_1
activate Interfaces Phase_1
activate Beams Phase_1
activate RigidBodies Phase_1
set (PositiveInterface_2_1.MaterialMode NegativeInterface_1_1.MaterialMode NegativeInterface_12_1.MaterialMode NegativeInterface_23_1.MaterialMode NegativeInterface_34_1.MaterialMode NegativeInterface_45_1.MaterialMode NegativeInterface_56_1.MaterialMode NegativeInterface_67_1.MaterialMode NegativeInterface_78_1.MaterialMode NegativeInterface_89_1.MaterialMode NegativeInterface_2_1.MaterialMode NegativeInterface_13_1.MaterialMode NegativeInterface_24_1.MaterialMode NegativeInterface_35_1.MaterialMode NegativeInterface_46_1.MaterialMode NegativeInterface_57_1.MaterialMode NegativeInterface_68_1.MaterialMode NegativeInterface_79_1.MaterialMode NegativeInterface_90_1.MaterialMode NegativeInterface_3_1.MaterialMode NegativeInterface_14_1.MaterialMode NegativeInterface_25_1.MaterialMode NegativeInterface_36_1.MaterialMode NegativeInterface_47_1.MaterialMode NegativeInterface_58_1.MaterialMode NegativeInterface_69_1.MaterialMode NegativeInterface_80_1.MaterialMode NegativeInterface_91_1.MaterialMode NegativeInterface_4_1.MaterialMode NegativeInterface_15_1.MaterialMode NegativeInterface_26_1.MaterialMode NegativeInterface_37_1.MaterialMode NegativeInterface_48_1.MaterialMode NegativeInterface_59_1.MaterialMode NegativeInterface_70_1.MaterialMode NegativeInterface_81_1.MaterialMode NegativeInterface_92_1.MaterialMode NegativeInterface_5_1.MaterialMode NegativeInterface_16_1.MaterialMode NegativeInterface_27_1.MaterialMode NegativeInterface_38_1.MaterialMode NegativeInterface_49_1.MaterialMode NegativeInterface_60_1.MaterialMode NegativeInterface_71_1.MaterialMode NegativeInterface_82_1.MaterialMode NegativeInterface_93_1.MaterialMode NegativeInterface_6_1.MaterialMode NegativeInterface_17_1.MaterialMode NegativeInterface_28_1.MaterialMode NegativeInterface_39_1.MaterialMode NegativeInterface_50_1.MaterialMode NegativeInterface_61_1.MaterialMode NegativeInterface_72_1.MaterialMode NegativeInterface_83_1.MaterialMode NegativeInterface_94_1.MaterialMode NegativeInterface_7_1.MaterialMode NegativeInterface_18_1.MaterialMode NegativeInterface_29_1.MaterialMode NegativeInterface_40_1.MaterialMode NegativeInterface_51_1.MaterialMode NegativeInterface_62_1.MaterialMode NegativeInterface_73_1.MaterialMode NegativeInterface_84_1.MaterialMode NegativeInterface_95_1.MaterialMode NegativeInterface_8_1.MaterialMode NegativeInterface_19_1.MaterialMode NegativeInterface_30_1.MaterialMode NegativeInterface_41_1.MaterialMode NegativeInterface_52_1.MaterialMode NegativeInterface_63_1.MaterialMode NegativeInterface_74_1.MaterialMode NegativeInterface_85_1.MaterialMode NegativeInterface_96_1.MaterialMode NegativeInterface_9_1.MaterialMode NegativeInterface_20_1.MaterialMode NegativeInterface_31_1.MaterialMode NegativeInterface_42_1.MaterialMode NegativeInterface_53_1.MaterialMode NegativeInterface_64_1.MaterialMode NegativeInterface_75_1.MaterialMode NegativeInterface_86_1.MaterialMode NegativeInterface_97_1.MaterialMode NegativeInterface_10_1.MaterialMode NegativeInterface_21_1.MaterialMode NegativeInterface_32_1.MaterialMode NegativeInterface_43_1.MaterialMode NegativeInterface_54_1.MaterialMode NegativeInterface_65_1.MaterialMode NegativeInterface_76_1.MaterialMode NegativeInterface_87_1.MaterialMode NegativeInterface_98_1.MaterialMode NegativeInterface_11_1.MaterialMode NegativeInterface_22_1.MaterialMode NegativeInterface_33_1.MaterialMode NegativeInterface_44_1.MaterialMode NegativeInterface_55_1.MaterialMode NegativeInterface_66_1.MaterialMode NegativeInterface_77_1.MaterialMode NegativeInterface_88_1.MaterialMode NegativeInterface_99_1.MaterialMode) Phase_1 "Custom"
set (PositiveInterface_2_1.Material NegativeInterface_1_1.Material NegativeInterface_12_1.Material NegativeInterface_23_1.Material NegativeInterface_34_1.Material NegativeInterface_45_1.Material NegativeInterface_56_1.Material NegativeInterface_67_1.Material NegativeInterface_78_1.Material NegativeInterface_89_1.Material NegativeInterface_2_1.Material NegativeInterface_13_1.Material NegativeInterface_24_1.Material NegativeInterface_35_1.Material NegativeInterface_46_1.Material NegativeInterface_57_1.Material NegativeInterface_68_1.Material NegativeInterface_79_1.Material NegativeInterface_90_1.Material NegativeInterface_3_1.Material NegativeInterface_14_1.Material NegativeInterface_25_1.Material NegativeInterface_36_1.Material NegativeInterface_47_1.Material NegativeInterface_58_1.Material NegativeInterface_69_1.Material NegativeInterface_80_1.Material NegativeInterface_91_1.Material NegativeInterface_4_1.Material NegativeInterface_15_1.Material NegativeInterface_26_1.Material NegativeInterface_37_1.Material NegativeInterface_48_1.Material NegativeInterface_59_1.Material NegativeInterface_70_1.Material NegativeInterface_81_1.Material NegativeInterface_92_1.Material NegativeInterface_5_1.Material NegativeInterface_16_1.Material NegativeInterface_27_1.Material NegativeInterface_38_1.Material NegativeInterface_49_1.Material NegativeInterface_60_1.Material NegativeInterface_71_1.Material NegativeInterface_82_1.Material NegativeInterface_93_1.Material NegativeInterface_6_1.Material NegativeInterface_17_1.Material NegativeInterface_28_1.Material NegativeInterface_39_1.Material NegativeInterface_50_1.Material NegativeInterface_61_1.Material NegativeInterface_72_1.Material NegativeInterface_83_1.Material NegativeInterface_94_1.Material NegativeInterface_7_1.Material NegativeInterface_18_1.Material NegativeInterface_29_1.Material NegativeInterface_40_1.Material NegativeInterface_51_1.Material NegativeInterface_62_1.Material NegativeInterface_73_1.Material NegativeInterface_84_1.Material NegativeInterface_95_1.Material NegativeInterface_8_1.Material NegativeInterface_19_1.Material NegativeInterface_30_1.Material NegativeInterface_41_1.Material NegativeInterface_52_1.Material NegativeInterface_63_1.Material NegativeInterface_74_1.Material NegativeInterface_85_1.Material NegativeInterface_96_1.Material NegativeInterface_9_1.Material NegativeInterface_20_1.Material NegativeInterface_31_1.Material NegativeInterface_42_1.Material NegativeInterface_53_1.Material NegativeInterface_64_1.Material NegativeInterface_75_1.Material NegativeInterface_86_1.Material NegativeInterface_97_1.Material NegativeInterface_10_1.Material NegativeInterface_21_1.Material NegativeInterface_32_1.Material NegativeInterface_43_1.Material NegativeInterface_54_1.Material NegativeInterface_65_1.Material NegativeInterface_76_1.Material NegativeInterface_87_1.Material NegativeInterface_98_1.Material NegativeInterface_11_1.Material NegativeInterface_22_1.Material NegativeInterface_33_1.Material NegativeInterface_44_1.Material NegativeInterface_55_1.Material NegativeInterface_66_1.Material NegativeInterface_77_1.Material NegativeInterface_88_1.Material NegativeInterface_99_1.Material) Phase_1 InterfaceForSoilZone_1
phase Phase_1
setproperties Phase_2 "Identification" "Small displacements"
set RigidBody_1_1.TranslationConditionx Phase_2 "Displacement"
set RigidBody_1_1.ux Phase_2 0.001204685462982295
phase Phase_1
setproperties Phase_3 "Identification" "Large displacements"
set RigidBody_1_1.TranslationConditionx Phase_3 "Displacement"
set RigidBody_1_1.ux Phase_3 1.204685462982295
setproperties Phase_1 "Solver" "Pardiso (multicore direct)"
setproperties Phase_2 "Deform.ResetDisplacementsToZero" True "Deform.UseDefaultIterationParams" False
setproperties Phase_2 "Deform.MaxLoadFractionPerStep" 0.02 "Deform.ToleratedError" 0.001 "Solver" "Pardiso (multicore direct)"
setproperties Phase_3 "Deform.ResetDisplacementsToZero" True "Deform.UseDefaultIterationParams" False
setproperties Phase_3 "Deform.ToleratedError" 0.01 "Solver" "Pardiso (multicore direct)" "Deform.MaxUnloadingSteps" 50 "Deform.MaxSteps" 10000 "Deform.MaxIterations" 90 "Deform.DesiredMinIterations" 4 "Deform.DesiredMaxIterations" 30
set (Phase_1.Deform.UseDefaultIterationParams Phase_2.Deform.UseDefaultIterationParams Phase_3.Deform.UseDefaultIterationParams) False
gotomesh
set (Surface_3_1.CoarsenessFactor Surface_1_1.CoarsenessFactor Surface_2_1.CoarsenessFactor Surface_4_1.CoarsenessFactor Surface_5_1.CoarsenessFactor Surface_6_1.CoarsenessFactor Surface_7_1.CoarsenessFactor Surface_8_1.CoarsenessFactor Surface_9_1.CoarsenessFactor Surface_10_1.CoarsenessFactor Surface_11_1.CoarsenessFactor Surface_12_1.CoarsenessFactor Surface_13_1.CoarsenessFactor Surface_14_1.CoarsenessFactor Surface_15_1.CoarsenessFactor Surface_16_1.CoarsenessFactor Surface_17_1.CoarsenessFactor Surface_18_1.CoarsenessFactor Surface_19_1.CoarsenessFactor Surface_20_1.CoarsenessFactor Surface_21_1.CoarsenessFactor Surface_22_1.CoarsenessFactor Surface_23_1.CoarsenessFactor Surface_24_1.CoarsenessFactor Surface_25_1.CoarsenessFactor Surface_26_1.CoarsenessFactor Surface_27_1.CoarsenessFactor Surface_28_1.CoarsenessFactor Surface_29_1.CoarsenessFactor Surface_30_1.CoarsenessFactor Surface_31_1.CoarsenessFactor Surface_32_1.CoarsenessFactor Surface_33_1.CoarsenessFactor Surface_34_1.CoarsenessFactor Surface_35_1.CoarsenessFactor Surface_36_1.CoarsenessFactor Surface_37_1.CoarsenessFactor Surface_38_1.CoarsenessFactor Surface_39_1.CoarsenessFactor Surface_40_1.CoarsenessFactor Surface_41_1.CoarsenessFactor Surface_42_1.CoarsenessFactor Surface_43_1.CoarsenessFactor Surface_44_1.CoarsenessFactor Surface_45_1.CoarsenessFactor Surface_46_1.CoarsenessFactor Surface_47_1.CoarsenessFactor Surface_48_1.CoarsenessFactor Surface_49_1.CoarsenessFactor Surface_50_1.CoarsenessFactor Surface_51_1.CoarsenessFactor Surface_52_1.CoarsenessFactor Surface_53_1.CoarsenessFactor Surface_54_1.CoarsenessFactor Surface_55_1.CoarsenessFactor Surface_56_1.CoarsenessFactor Surface_57_1.CoarsenessFactor Surface_58_1.CoarsenessFactor Surface_59_1.CoarsenessFactor Surface_60_1.CoarsenessFactor Surface_61_1.CoarsenessFactor Surface_62_1.CoarsenessFactor Surface_63_1.CoarsenessFactor Surface_64_1.CoarsenessFactor Surface_65_1.CoarsenessFactor Surface_66_1.CoarsenessFactor Surface_67_1.CoarsenessFactor Surface_68_1.CoarsenessFactor Surface_69_1.CoarsenessFactor Surface_70_1.CoarsenessFactor Surface_71_1.CoarsenessFactor Surface_72_1.CoarsenessFactor Surface_73_1.CoarsenessFactor Surface_74_1.CoarsenessFactor Surface_75_1.CoarsenessFactor Surface_76_1.CoarsenessFactor Surface_77_1.CoarsenessFactor Surface_78_1.CoarsenessFactor Surface_79_1.CoarsenessFactor Surface_80_1.CoarsenessFactor Surface_81_1.CoarsenessFactor Surface_82_1.CoarsenessFactor Surface_83_1.CoarsenessFactor Surface_84_1.CoarsenessFactor Surface_85_1.CoarsenessFactor Surface_86_1.CoarsenessFactor Surface_87_1.CoarsenessFactor Surface_88_1.CoarsenessFactor Surface_89_1.CoarsenessFactor Surface_90_1.CoarsenessFactor Surface_91_1.CoarsenessFactor Surface_92_1.CoarsenessFactor Surface_93_1.CoarsenessFactor Surface_94_1.CoarsenessFactor Surface_95_1.CoarsenessFactor Surface_96_1.CoarsenessFactor Surface_97_1.CoarsenessFactor Surface_98_1.CoarsenessFactor Surface_99_1.CoarsenessFactor Surface_100_1.CoarsenessFactor Surface_101_1.CoarsenessFactor Surface_102_1.CoarsenessFactor) 1.0
set (Line_1_1.CoarsenessFactor Line_2_1.CoarsenessFactor) 1.0
set (Surface_3_1.CoarsenessFactor) 0.07
mesh 0.075 256 True
selectmeshpoints
gotostages
checkcalculationconditions
validate SoilZone_1
validate InterfaceForSoilZone_1
validate Plate_0038
validate Beam_0038
_sps SoilZone_1 "Comments" "" "Metadata" "" "MaterialName" "SoilZone_1" "Colour" 15262369 "MaterialNumber" 1 "SoilModel" 4 "UserDefinedIndex" 0 "DrainageType" 0 "DilatancyCutOff" False "UndrainedBehaviour" 0 "InterfaceStrength" 0 "InterfaceStiffness" 0 "ConsiderGapClosure" False "K0PrimaryIsK0Secondary" True "K0Determination" 0 "SolidThermalExpansion" 1 "CrossPermeability" 0 "DefaultValuesAdvanced" False "DataSetFlow" 0 "ModelFlow" 0 "UDModelFlow" 0 "SoilTypeFlow" 0 "LowerUpper" 0 "UsdaSoilType" 0 "StaringUpperSoilType" 0 "StaringLowerSoilType" 0 "M50" 0 "UseDefaultsFlow" 0 "TablePsiPermSat" "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]" "SplinePsiPerm" "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]" "SplinePsiSat" "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]" "UseAlternatives" False "TensionCutOff" True "FailureCriterion" 0 "einit" 0.5 "emin" 0 "emax" 999 "SkemptonB" 0.986622073578595 "KwRefN" 5531250 "VolumetricSpecificStorage" 1.80790960451978E-6 "DrainageConductivity1" 0 "DrainageConductivity2" 0 "EurRef" 135000 "ErefOed50" 1 "ErefUr50" 3 "Cc" 0.00766666666666667 "Cs" 0.0023 56250 0.2 39 5 9 0 0 0 19.9 19.9 0 0 1 0 0 0 0 0 0 0.333333333333333 0 0.999 0 0 0 0 1.0000000000000000E+015 0.495 0 0 2.27389442804142 1.67839452491998 0 0.5 100 36265.7292128222 0.875 45000 0.370679608950163 45000 0 0 0 0 0 0 0 0 194000 0.000125 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0.5 0.5 1 0 1 -1.06 -2.37 0 0 10000 1 0.0620347394540943 3.83 1.3774 1.25 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 10 13 77 0 0 0 0 0 0 0
_sps InterfaceForSoilZone_1 "Comments" "" "Metadata" "" "MaterialName" "InterfaceForSoilZone_1" "Colour" 10676870 "MaterialNumber" 2 "SoilModel" 4 "UserDefinedIndex" 0 "DrainageType" 0 "DilatancyCutOff" False "UndrainedBehaviour" 0 "InterfaceStrength" 0 "InterfaceStiffness" 0 "ConsiderGapClosure" False "K0PrimaryIsK0Secondary" True "K0Determination" 0 "SolidThermalExpansion" 1 "CrossPermeability" 0 "DefaultValuesAdvanced" False "DataSetFlow" 0 "ModelFlow" 0 "UDModelFlow" 0 "SoilTypeFlow" 0 "LowerUpper" 0 "UsdaSoilType" 0 "StaringUpperSoilType" 0 "StaringLowerSoilType" 0 "M50" 0 "UseDefaultsFlow" 0 "TablePsiPermSat" "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]" "SplinePsiPerm" "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]" "SplinePsiSat" "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]" "UseAlternatives" False "TensionCutOff" True "FailureCriterion" 0 "einit" 0.5 "emin" 0 "emax" 999 "SkemptonB" 0.986622073578595 "KwRefN" 5531250 "VolumetricSpecificStorage" 1.80790960451978E-6 "DrainageConductivity1" 0 "DrainageConductivity2" 0 "EurRef" 135000 "ErefOed50" 1 "ErefUr50" 3 "Cc" 0.00766666666666667 "Cs" 0.0023 56250 0.2 39 5 9 0 0 0 17 17 0 0 1 0 0 0 0 0 0 0.333333333333333 0 0.999 0 0 0 0 1.0000000000000000E+015 0.495 0 0 2.27389442804142 1.67839452491998 0 0.5 100 36265.7292128222 0.875 45000 0.370679608950163 45000 0 0 0 0 0 0 0 0 194000 0.000125 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0.5 0.5 1 0 1 -1.06 -2.37 0 0 10000 1 0.0620347394540943 3.83 1.3774 1.25 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 10 13 77 0 0 0 0 0 0 0
gotostages
set InitialPhase.ShouldCalculate True
set Phase_1.ShouldCalculate True
set Phase_2.ShouldCalculate True
set Phase_3.ShouldCalculate True
calculate
_set Model.CurrentPhase Phase_3
_set Model.CurrentPhase Phase_2
_gotomesh
_gotowater
_gotostages
_set Model.CurrentPhase Phase_1
_set Phase_1.ShouldCalculate True
_set Model.CurrentPhase Phase_2
_set Phase_2.MaxStepsStored 10000
_set Model.CurrentPhase Phase_3
_set Phase_3.MaxStepsStored 1000
_set Phase_3.MaxStepsStored 10000
_save "D:\Shamsher\Final_manscripts\Monopile\Monopile_Mcadam_Dunirk site_Halfmodel.p3d"
_set Model.CurrentPhase Phase_1
_set Model.CurrentPhase Phase_2
_set Model.CurrentPhase Phase_1
_selectmeshpoints
_calculate
_save "D:\Shamsher\Final_manscripts\Monopile\Monopile_Mcadam_Dunirk site_Halfmodel.p3d"
_view Phase_1
_gotosoil
_gotostructures
_gotostages
_view Phase_1
_view Phase_1
_gotosoil
_gotostructures
_gotostages
_gotostructures
_polycurve 0 0 0 1 0 0 0 1 0
_add Polycurve_1
_set Polycurve_1.Segments[0].SegmentType "Arc"
_set Polycurve_1.Segments[0].ArcProperties.CentralAngle 180
_set Polycurve_1.Segments[0].ArcProperties.Radius 0.2
_set Polycurve_1.Offset1 1
_set Polycurve_1.Offset1 0
_set Polycurve_1.OrientationAxis1X 0
_set Polycurve_1.OrientationAxis1Y 1
_set Polycurve_1.OrientationAxis1Y 0
_set Polycurve_1.OrientationAxis1Z 1
_set Polycurve_1.OrientationAxis1X 1
_set Polycurve_1.OrientationAxis1Z 0
_set Polycurve_1.OrientationAxis2X 1
_set Polycurve_1.OrientationAxis2Y 0
_set Polycurve_1.OrientationAxis2X 0
_set Polycurve_1.OrientationAxis2Z 1
_set Polycurve_1.OrientationAxis2Y 1
_set Polycurve_1.OrientationAxis2Z 0
_set Polycurve_1.OrientationAxis1X 0
_set Polycurve_1.OrientationAxis1Y 1
_set Polycurve_1.OrientationAxis1X 1
_set Polycurve_1.OrientationAxis1Y 0
_delete Geometry Polycurve_1
_polycurve 0 0 0 1 0 0 0 1 0
_set Polycurve_1.OrientationAxis1X 0
_set Polycurve_1.OrientationAxis1Y 1
_add Polycurve_1
_set Polycurve_1.Segments[0].SegmentType "Arc"
_set Polycurve_1.Segments[0].ArcProperties.CentralAngle 180
_set Polycurve_1.Segments[0].ArcProperties.Radius 0.2
_set Polycurve_1.OrientationAxis2X 1
_set Polycurve_1.OrientationAxis2Y 0
_set Polycurve_1.Offset1 0.1
_set Polycurve_1.Offset1 0
_set Polycurve_1.x 0.1
_set Polycurve_1.x -0.1
_set Polycurve_1.Segments[0].ArcProperties.Radius 0.1
_extrude (Polycurve_1) 0 0 -1
_add Polycurve_1
_set Polycurve_1.Segments[1].LineProperties.RelativeStartAngle1 90
_set Polycurve_1.Segments[1].LineProperties.Length 0.1
_set Polycurve_1.Segments[1].LineProperties.Length 0.2
_surface Polycurve_1
_delete Geometry Surface_103
_extrude (Polycurve_1) 0 0 -1
_rigidbody (Surface_104 Surface_103)
_set Surface_104.RigidBody.Xref 0
_gotomesh
_mesh 0.075 256 True 1.2 0.005
_gotowater
_gotostages
_set Model.CurrentPhase Phase_2
_set Model.CurrentPhase Phase_1
_undo
_set Model.CurrentPhase Phase_3
_set Phase_3.ShouldCalculate True
_set Model.CurrentPhase InitialPhase
_set Model.CurrentPhase Phase_1
_activate RigidBody_2 Phase_1
_activate RigidBody_3 Phase_1
_set (RigidBody_3_4.Zref RigidBody_3_3.Zref RigidBody_3_2.Zref RigidBody_3_1.Zref) Phase_1 0
_set (RigidBody_3_4.Xref RigidBody_3_3.Xref RigidBody_3_2.Xref RigidBody_3_1.Xref) Phase_1 0
_set Model.CurrentPhase Phase_2
_activate RigidBody_2 Phase_2
_activate RigidBody_3 Phase_2
_set (RigidBody_3_4.Zref RigidBody_3_3.Zref RigidBody_3_2.Zref RigidBody_3_1.Zref) Phase_2 0
_set (RigidBody_3_4.Xref RigidBody_3_3.Xref RigidBody_3_2.Xref RigidBody_3_1.Xref) Phase_2 0
_set Model.CurrentPhase Phase_3
_activate RigidBody_2 Phase_3
_activate RigidBody_3 Phase_3
_set (RigidBody_3_4.Zref RigidBody_3_3.Zref RigidBody_3_2.Zref RigidBody_3_1.Zref) Phase_3 0
_set (RigidBody_3_4.Xref RigidBody_3_3.Xref RigidBody_3_2.Xref RigidBody_3_1.Xref) Phase_3 0
_save "D:\Shamsher\Final_manscripts\Monopile\Monopile_Mcadam_Dunirk site_Halfmodel.p3d"
_set Model.CurrentPhase Phase_2
_set Model.CurrentPhase Phase_3
_set Model.CurrentPhase Phase_2
_set Phase_2.ShouldCalculate False
_set Model.CurrentPhase Phase_3
_calculate
_view Phase_3
_set Phase_3.ShouldCalculate True
_set Phase_3.ShouldCalculate False
##~ running Plaxis3DInput.exe 20.0.0.119
_view Phase_3
