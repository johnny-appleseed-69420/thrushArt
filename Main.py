#My script imports
from Pixelsorting import pixelsorter
from UserInput import userInput

#greeting
print("Hello and welcome to the Thrush Band Incorporated Image Pulverizer.  Please insert tip.\n\n")

#runs userinput script, then pixelsorter script
input_path, output_path = userInput()
pixelsorter(input_path, output_path)