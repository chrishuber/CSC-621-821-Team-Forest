import itk
import argparse


# ITK requires that input images start with '-' for some reason.
input_image = "-original.jpg"
output_image = "-output.jpg"

# This section just takes converts the iput above to ITK usable objects
parser = argparse.ArgumentParser()
parser.add_argument(input_image)
parser.add_argument(output_image)
args = parser.parse_args()

#Each pixel is 1 unsigned char or 1 byte
PixelType = itk.UC

# It's a 2D image
Dimension = 2

# Creates Image object
ImageType = itk.Image[PixelType, Dimension]

# Rendering Image object as an image
ReaderType = itk.ImageFileReader[ImageType]
reader = ReaderType.New()
reader.SetFileName(input_image)

# Creating an RGB "layer"
RGBPixelType = itk.RGBPixel[PixelType]
RGBImageType = itk.Image[RGBPixelType, Dimension]

# Looks confusing, but basically it just applies a rgb filter over the image.
# Here is a list of predefined enum values.
# Replace the suffix of colorMap_Filter to apply.
# Ex: RGBColormapFilter_Hot -> RGBColormapFilter_Blue
# Colors:
#   Red,
#   Green
#   Blue
#   Grey
#   Hot
#   Cool
#   Spring
#   Summer
#   Autumn
#   Winter
#   Copper
#   Jet
#   HSV
#   OverUnder

colorMap_Filter = itk.ScalarToRGBColormapImageFilterEnums.RGBColormapFilter_Winter

RGBFilterType = itk.ScalarToRGBColormapImageFilter[ImageType, RGBImageType]
rgbfilter = RGBFilterType.New()
rgbfilter.SetInput(reader.GetOutput())
rgbfilter.SetColormap(colorMap_Filter)

# Renders the final result into an image
WriterType = itk.ImageFileWriter[RGBImageType]
writer = WriterType.New()
# writer.SetFileName(args.output_image)
writer.SetFileName(output_image)
writer.SetInput(rgbfilter.GetOutput())

writer.Update()