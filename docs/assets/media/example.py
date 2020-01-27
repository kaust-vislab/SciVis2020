# state file generated using paraview version 5.7.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [2480, 1645]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [40.00709915161133, 20.007100105285645, -0.39749999667401426]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [40.64467836216293, -6.236895131686442, 21.040090455154008]
renderView1.CameraFocalPoint = [39.763038435645306, 21.653261287692988, -3.6523612758508794]
renderView1.CameraViewUp = [0.0028364362976702404, 0.662928504434218, 0.7486773354641775]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 14.1194337619734
renderView1.Background = [0.32, 0.34, 0.43]
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
cOMBINED_2011013100nc = NetCDFReader(FileName=['SciVisContest2020/ensembles/0001/COMBINED_2011013100.nc'])
cOMBINED_2011013100nc.Dimensions = '(Z_MIT40, YG, XC)'
cOMBINED_2011013100nc.SphericalCoordinates = 0

# create a new 'NetCDF Reader'
cOMBINED_2011013100nc_1 = NetCDFReader(FileName=['SciVisContest2020/ensembles/0001/COMBINED_2011013100.nc'])
cOMBINED_2011013100nc_1.Dimensions = '(Z_MIT40, YC, XC)'
cOMBINED_2011013100nc_1.SphericalCoordinates = 0

# create a new 'NetCDF Reader'
cOMBINED_2011013100nc_2 = NetCDFReader(FileName=['SciVisContest2020/ensembles/0001/COMBINED_2011013100.nc'])
cOMBINED_2011013100nc_2.Dimensions = '(Z_MIT40, YC, XG)'
cOMBINED_2011013100nc_2.SphericalCoordinates = 0

# create a new 'XDMF Reader'
bathymetryxmf = XDMFReader(FileNames=['SciVisContest2020/bathymetry.xmf'])
bathymetryxmf.PointArrayStatus = ['depth']
bathymetryxmf.GridStatus = ['Grid']

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=bathymetryxmf)
warpByScalar1.Scalars = ['POINTS', 'depth']
warpByScalar1.ScaleFactor = 0.00025

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(Input=[cOMBINED_2011013100nc_1, cOMBINED_2011013100nc_2, cOMBINED_2011013100nc])

# create a new 'Calculator'
calculator1 = Calculator(Input=appendAttributes1)
calculator1.ResultArrayName = 'UVW'
calculator1.Function = 'U*iHat + V*jHat + W*kHat'

# create a new 'Transform'
transform1 = Transform(Input=calculator1)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Scale = [1.0, 1.0, 0.00025]

# create a new 'Glyph'
glyph1 = Glyph(Input=transform1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'UVW']
glyph1.ScaleArray = ['POINTS', 'UVW']
glyph1.ScaleFactor = 1.996000099182129
glyph1.GlyphTransform = 'Transform2'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from cOMBINED_2011013100nc_1
cOMBINED_2011013100nc_1Display = Show(cOMBINED_2011013100nc_1, renderView1)

# trace defaults for the display properties.
cOMBINED_2011013100nc_1Display.Representation = 'Outline'
cOMBINED_2011013100nc_1Display.ColorArrayName = [None, '']
cOMBINED_2011013100nc_1Display.OSPRayScaleArray = 'SALT'
cOMBINED_2011013100nc_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cOMBINED_2011013100nc_1Display.SelectOrientationVectors = 'None'
cOMBINED_2011013100nc_1Display.ScaleFactor = 317.6
cOMBINED_2011013100nc_1Display.SelectScaleArray = 'None'
cOMBINED_2011013100nc_1Display.GlyphType = 'Arrow'
cOMBINED_2011013100nc_1Display.GlyphTableIndexArray = 'None'
cOMBINED_2011013100nc_1Display.GaussianRadius = 15.88
cOMBINED_2011013100nc_1Display.SetScaleArray = ['POINTS', 'SALT']
cOMBINED_2011013100nc_1Display.ScaleTransferFunction = 'PiecewiseFunction'
cOMBINED_2011013100nc_1Display.OpacityArray = ['POINTS', 'SALT']
cOMBINED_2011013100nc_1Display.OpacityTransferFunction = 'PiecewiseFunction'
cOMBINED_2011013100nc_1Display.DataAxesGrid = 'GridAxesRepresentation'
cOMBINED_2011013100nc_1Display.PolarAxes = 'PolarAxesRepresentation'
cOMBINED_2011013100nc_1Display.SelectInputVectors = [None, '']
cOMBINED_2011013100nc_1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cOMBINED_2011013100nc_1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 42.474082946777344, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cOMBINED_2011013100nc_1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 42.474082946777344, 1.0, 0.5, 0.0]

# show data from cOMBINED_2011013100nc_2
cOMBINED_2011013100nc_2Display = Show(cOMBINED_2011013100nc_2, renderView1)

# trace defaults for the display properties.
cOMBINED_2011013100nc_2Display.Representation = 'Outline'
cOMBINED_2011013100nc_2Display.ColorArrayName = [None, '']
cOMBINED_2011013100nc_2Display.OSPRayScaleArray = 'U'
cOMBINED_2011013100nc_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
cOMBINED_2011013100nc_2Display.SelectOrientationVectors = 'None'
cOMBINED_2011013100nc_2Display.ScaleFactor = 317.6
cOMBINED_2011013100nc_2Display.SelectScaleArray = 'None'
cOMBINED_2011013100nc_2Display.GlyphType = 'Arrow'
cOMBINED_2011013100nc_2Display.GlyphTableIndexArray = 'None'
cOMBINED_2011013100nc_2Display.GaussianRadius = 15.88
cOMBINED_2011013100nc_2Display.SetScaleArray = ['POINTS', 'U']
cOMBINED_2011013100nc_2Display.ScaleTransferFunction = 'PiecewiseFunction'
cOMBINED_2011013100nc_2Display.OpacityArray = ['POINTS', 'U']
cOMBINED_2011013100nc_2Display.OpacityTransferFunction = 'PiecewiseFunction'
cOMBINED_2011013100nc_2Display.DataAxesGrid = 'GridAxesRepresentation'
cOMBINED_2011013100nc_2Display.PolarAxes = 'PolarAxesRepresentation'
cOMBINED_2011013100nc_2Display.SelectInputVectors = [None, '']
cOMBINED_2011013100nc_2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cOMBINED_2011013100nc_2Display.ScaleTransferFunction.Points = [-0.7852849364280701, 0.0, 0.5, 0.0, 0.8659229278564453, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cOMBINED_2011013100nc_2Display.OpacityTransferFunction.Points = [-0.7852849364280701, 0.0, 0.5, 0.0, 0.8659229278564453, 1.0, 0.5, 0.0]

# show data from cOMBINED_2011013100nc
cOMBINED_2011013100ncDisplay = Show(cOMBINED_2011013100nc, renderView1)

# trace defaults for the display properties.
cOMBINED_2011013100ncDisplay.Representation = 'Outline'
cOMBINED_2011013100ncDisplay.ColorArrayName = [None, '']
cOMBINED_2011013100ncDisplay.OSPRayScaleArray = 'V'
cOMBINED_2011013100ncDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cOMBINED_2011013100ncDisplay.SelectOrientationVectors = 'None'
cOMBINED_2011013100ncDisplay.ScaleFactor = 317.6
cOMBINED_2011013100ncDisplay.SelectScaleArray = 'None'
cOMBINED_2011013100ncDisplay.GlyphType = 'Arrow'
cOMBINED_2011013100ncDisplay.GlyphTableIndexArray = 'None'
cOMBINED_2011013100ncDisplay.GaussianRadius = 15.88
cOMBINED_2011013100ncDisplay.SetScaleArray = ['POINTS', 'V']
cOMBINED_2011013100ncDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cOMBINED_2011013100ncDisplay.OpacityArray = ['POINTS', 'V']
cOMBINED_2011013100ncDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cOMBINED_2011013100ncDisplay.DataAxesGrid = 'GridAxesRepresentation'
cOMBINED_2011013100ncDisplay.PolarAxes = 'PolarAxesRepresentation'
cOMBINED_2011013100ncDisplay.SelectInputVectors = [None, '']
cOMBINED_2011013100ncDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cOMBINED_2011013100ncDisplay.ScaleTransferFunction.Points = [-0.931229293346405, 0.0, 0.5, 0.0, 0.7413023710250854, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cOMBINED_2011013100ncDisplay.OpacityTransferFunction.Points = [-0.931229293346405, 0.0, 0.5, 0.0, 0.7413023710250854, 1.0, 0.5, 0.0]

# show data from appendAttributes1
appendAttributes1Display = Show(appendAttributes1, renderView1)

# trace defaults for the display properties.
appendAttributes1Display.Representation = 'Outline'
appendAttributes1Display.ColorArrayName = [None, '']
appendAttributes1Display.OSPRayScaleArray = 'SALT'
appendAttributes1Display.OSPRayScaleFunction = 'PiecewiseFunction'
appendAttributes1Display.SelectOrientationVectors = 'None'
appendAttributes1Display.ScaleFactor = 317.6
appendAttributes1Display.SelectScaleArray = 'None'
appendAttributes1Display.GlyphType = 'Arrow'
appendAttributes1Display.GlyphTableIndexArray = 'None'
appendAttributes1Display.GaussianRadius = 15.88
appendAttributes1Display.SetScaleArray = ['POINTS', 'SALT']
appendAttributes1Display.ScaleTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.OpacityArray = ['POINTS', 'SALT']
appendAttributes1Display.OpacityTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.DataAxesGrid = 'GridAxesRepresentation'
appendAttributes1Display.PolarAxes = 'PolarAxesRepresentation'
appendAttributes1Display.SelectInputVectors = [None, '']
appendAttributes1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
appendAttributes1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 42.474082946777344, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
appendAttributes1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 42.474082946777344, 1.0, 0.5, 0.0]

# show data from calculator1
calculator1Display = Show(calculator1, renderView1)

# trace defaults for the display properties.
calculator1Display.Representation = 'Outline'
calculator1Display.ColorArrayName = [None, '']
calculator1Display.OSPRayScaleArray = 'Result'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'Result'
calculator1Display.ScaleFactor = 317.6
calculator1Display.SelectScaleArray = 'None'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'None'
calculator1Display.GaussianRadius = 15.88
calculator1Display.SetScaleArray = ['POINTS', 'Result']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'Result']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.SelectInputVectors = ['POINTS', 'Result']
calculator1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-0.7852849364280701, 0.0, 0.5, 0.0, 0.8659229278564453, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-0.7852849364280701, 0.0, 0.5, 0.0, 0.8659229278564453, 1.0, 0.5, 0.0]

# show data from transform1
transform1Display = Show(transform1, renderView1)

# trace defaults for the display properties.
transform1Display.Representation = 'Outline'
transform1Display.ColorArrayName = [None, '']
transform1Display.OSPRayScaleArray = 'SALT'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'UVW'
transform1Display.ScaleFactor = 1.996000099182129
transform1Display.SelectScaleArray = 'None'
transform1Display.GlyphType = 'Arrow'
transform1Display.GlyphTableIndexArray = 'None'
transform1Display.GaussianRadius = 0.09980000495910644
transform1Display.SetScaleArray = ['POINTS', 'SALT']
transform1Display.ScaleTransferFunction = 'PiecewiseFunction'
transform1Display.OpacityArray = ['POINTS', 'SALT']
transform1Display.OpacityTransferFunction = 'PiecewiseFunction'
transform1Display.DataAxesGrid = 'GridAxesRepresentation'
transform1Display.PolarAxes = 'PolarAxesRepresentation'
transform1Display.ScalarOpacityUnitDistance = 0.12266336815460342
transform1Display.SelectInputVectors = ['POINTS', 'UVW']
transform1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 42.474082946777344, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 42.474082946777344, 1.0, 0.5, 0.0]

# show data from bathymetryxmf
bathymetryxmfDisplay = Show(bathymetryxmf, renderView1)

# get color transfer function/color map for 'depth'
depthLUT = GetColorTransferFunction('depth')
depthLUT.RGBPoints = [-3073.121826171875, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0]
depthLUT.ColorSpace = 'RGB'
depthLUT.NanColor = [1.0, 0.0, 0.0]
depthLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'depth'
depthPWF = GetOpacityTransferFunction('depth')
depthPWF.Points = [-3073.121826171875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]
depthPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
bathymetryxmfDisplay.Representation = 'Slice'
bathymetryxmfDisplay.ColorArrayName = ['POINTS', 'depth']
bathymetryxmfDisplay.LookupTable = depthLUT
bathymetryxmfDisplay.OSPRayScaleArray = 'depth'
bathymetryxmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
bathymetryxmfDisplay.SelectOrientationVectors = 'None'
bathymetryxmfDisplay.ScaleFactor = 1.9960000000000002
bathymetryxmfDisplay.SelectScaleArray = 'depth'
bathymetryxmfDisplay.GlyphType = 'Arrow'
bathymetryxmfDisplay.GlyphTableIndexArray = 'depth'
bathymetryxmfDisplay.GaussianRadius = 0.0998
bathymetryxmfDisplay.SetScaleArray = ['POINTS', 'depth']
bathymetryxmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
bathymetryxmfDisplay.OpacityArray = ['POINTS', 'depth']
bathymetryxmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'
bathymetryxmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
bathymetryxmfDisplay.PolarAxes = 'PolarAxesRepresentation'
bathymetryxmfDisplay.ScalarOpacityUnitDistance = 0.4486852963400412
bathymetryxmfDisplay.ScalarOpacityFunction = depthPWF
bathymetryxmfDisplay.IsosurfaceValues = [-1536.5609130859375]
bathymetryxmfDisplay.SelectInputVectors = [None, '']
bathymetryxmfDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
bathymetryxmfDisplay.ScaleTransferFunction.Points = [-3073.121826171875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
bathymetryxmfDisplay.OpacityTransferFunction.Points = [-3073.121826171875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# show data from warpByScalar1
warpByScalar1Display = Show(warpByScalar1, renderView1)

# trace defaults for the display properties.
warpByScalar1Display.Representation = 'Surface'
warpByScalar1Display.ColorArrayName = ['POINTS', 'depth']
warpByScalar1Display.LookupTable = depthLUT
warpByScalar1Display.OSPRayScaleArray = 'depth'
warpByScalar1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByScalar1Display.SelectOrientationVectors = 'None'
warpByScalar1Display.ScaleFactor = 1.996000099182129
warpByScalar1Display.SelectScaleArray = 'depth'
warpByScalar1Display.GlyphType = 'Arrow'
warpByScalar1Display.GlyphTableIndexArray = 'depth'
warpByScalar1Display.GaussianRadius = 0.09980000495910644
warpByScalar1Display.SetScaleArray = ['POINTS', 'depth']
warpByScalar1Display.ScaleTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.OpacityArray = ['POINTS', 'depth']
warpByScalar1Display.OpacityTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByScalar1Display.PolarAxes = 'PolarAxesRepresentation'
warpByScalar1Display.ScalarOpacityFunction = depthPWF
warpByScalar1Display.ScalarOpacityUnitDistance = 0.4488514546883703
warpByScalar1Display.SelectInputVectors = [None, '']
warpByScalar1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
warpByScalar1Display.ScaleTransferFunction.Points = [-3073.121826171875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
warpByScalar1Display.OpacityTransferFunction.Points = [-3073.121826171875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# show data from glyph1
glyph1Display = Show(glyph1, renderView1)

# get color transfer function/color map for 'TEMP'
tEMPLUT = GetColorTransferFunction('TEMP')
tEMPLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 15.086803436279297, 0.865003, 0.865003, 0.865003, 30.173606872558594, 0.705882, 0.0156863, 0.14902]
tEMPLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'TEMP']
glyph1Display.LookupTable = tEMPLUT
glyph1Display.OSPRayScaleArray = 'SALT'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 2.1955997467041017
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.10977998733520508
glyph1Display.SetScaleArray = ['POINTS', 'SALT']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'SALT']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'
glyph1Display.SelectInputVectors = [None, '']
glyph1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.65577697753906, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.65577697753906, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color transfer function/color map for 'ImageFile'
imageFileLUT = GetColorTransferFunction('ImageFile')
imageFileLUT.RGBPoints = [-3073.121826171875, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0]
imageFileLUT.ColorSpace = 'RGB'
imageFileLUT.NanColor = [1.0, 0.0, 0.0]
imageFileLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for imageFileLUT in view renderView1
imageFileLUTColorBar = GetScalarBar(imageFileLUT, renderView1)
imageFileLUTColorBar.Title = 'ImageFile'
imageFileLUTColorBar.ComponentTitle = ''

# set color bar visibility
imageFileLUTColorBar.Visibility = 0

# get color transfer function/color map for 'ETA'
eTALUT = GetColorTransferFunction('ETA')
eTALUT.RGBPoints = [-0.16954773664474487, 0.231373, 0.298039, 0.752941, 0.025052733719348907, 0.865003, 0.865003, 0.865003, 0.2196532040834427, 0.705882, 0.0156863, 0.14902]
eTALUT.ScalarRangeInitialized = 1.0

# get color legend/bar for eTALUT in view renderView1
eTALUTColorBar = GetScalarBar(eTALUT, renderView1)
eTALUTColorBar.Title = 'ETA'
eTALUTColorBar.ComponentTitle = ''

# set color bar visibility
eTALUTColorBar.Visibility = 0

# get color legend/bar for depthLUT in view renderView1
depthLUTColorBar = GetScalarBar(depthLUT, renderView1)
depthLUTColorBar.Title = 'depth'
depthLUTColorBar.ComponentTitle = ''

# set color bar visibility
depthLUTColorBar.Visibility = 0

# get color transfer function/color map for 'TiffScalars'
tiffScalarsLUT = GetColorTransferFunction('TiffScalars')
tiffScalarsLUT.RGBPoints = [-3073.121826171875, 0.231373, 0.298039, 0.752941, -1536.5609130859375, 0.865003, 0.865003, 0.865003, 0.0, 0.705882, 0.0156863, 0.14902]
tiffScalarsLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for tiffScalarsLUT in view renderView1
tiffScalarsLUTColorBar = GetScalarBar(tiffScalarsLUT, renderView1)
tiffScalarsLUTColorBar.Title = 'Tiff Scalars'
tiffScalarsLUTColorBar.ComponentTitle = ''

# set color bar visibility
tiffScalarsLUTColorBar.Visibility = 0

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.AnnotationsInitialized = 1
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.ActiveAnnotatedValues = ['0', '1', '2']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]

# get color legend/bar for vtkBlockColorsLUT in view renderView1
vtkBlockColorsLUTColorBar = GetScalarBar(vtkBlockColorsLUT, renderView1)
vtkBlockColorsLUTColorBar.Title = 'vtkBlockColors'
vtkBlockColorsLUTColorBar.ComponentTitle = ''

# set color bar visibility
vtkBlockColorsLUTColorBar.Visibility = 0

# get color legend/bar for tEMPLUT in view renderView1
tEMPLUTColorBar = GetScalarBar(tEMPLUT, renderView1)
tEMPLUTColorBar.WindowLocation = 'AnyLocation'
tEMPLUTColorBar.Position = [0.8995967741935484, 0.6382978723404255]
tEMPLUTColorBar.Title = 'TEMP'
tEMPLUTColorBar.ComponentTitle = ''
tEMPLUTColorBar.ScalarBarLength = 0.32999999999999985

# set color bar visibility
tEMPLUTColorBar.Visibility = 1

# hide data in view
Hide(cOMBINED_2011013100nc_1, renderView1)

# hide data in view
Hide(cOMBINED_2011013100nc_2, renderView1)

# hide data in view
Hide(cOMBINED_2011013100nc, renderView1)

# hide data in view
Hide(appendAttributes1, renderView1)

# hide data in view
Hide(calculator1, renderView1)

# hide data in view
Hide(bathymetryxmf, renderView1)

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'TiffScalars'
tiffScalarsPWF = GetOpacityTransferFunction('TiffScalars')
tiffScalarsPWF.Points = [-3073.121826171875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]
tiffScalarsPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'TEMP'
tEMPPWF = GetOpacityTransferFunction('TEMP')
tEMPPWF.Points = [0.0, 0.0, 0.5, 0.0, 30.173606872558594, 1.0, 0.5, 0.0]
tEMPPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'ImageFile'
imageFilePWF = GetOpacityTransferFunction('ImageFile')
imageFilePWF.Points = [-3073.121826171875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]
imageFilePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'ETA'
eTAPWF = GetOpacityTransferFunction('ETA')
eTAPWF.Points = [-0.16954773664474487, 0.0, 0.5, 0.0, 0.2196532040834427, 1.0, 0.5, 0.0]
eTAPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(warpByScalar1)
# ----------------------------------------------------------------
