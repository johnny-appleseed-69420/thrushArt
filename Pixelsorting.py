from pixelsort import pixelsort
from PIL import Image

#Basic Pixelsorting
def pixelsorter(input_path, output_path):
    try:
        #f-string is more concise than concatenation
        print(f"Attempting to open: {input_path}") 

        #This is the image that will get sorted
        theImage = Image.open(input_path) 

        #conducts the actual pixelsorting
        sortedImage = pixelsort(theImage)

        #save the image to output path
        sortedImage.save(output_path)
        print("image has been saved to " + output_path)

    except OSError:
        print("OSError, File not found")

    except:
        print("Something went wrong")
