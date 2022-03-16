HOW TO RUN

1. pip3 install itk
2. cd into the segmentation folder.
3. run python3 WatershedSegmentation.py BrainProtonDensitySlice.png OutBrainWatershed.png 0.005 .5
4. Your output image can be found in the segmentation folder.
BrainProtonDensitySlice.png is our input to the program. 
OutBrainWatershed is our the name of the segmented image the program will produce. 
0.005 and .5 are paramters passed to the program that dictate the level of segmentation. 
Review this URL for more information.
https://itk.org/ITKExamples/src/Segmentation/Watersheds/SegmentWithWatershedImageFilter/Documentation.html
