#My script imports
from Pixelsorting import pixelsorter, foldersorter
from UserInput import userInput
from dotenv import load_dotenv
import os

load_dotenv()#testing
directory = os.getenv("\n\n\nfolder_input_path")

# Print to check if it's correct
print(f"Directory path: {directory}")
#greeting
print("Hello and welcome to the Thrush Band Incorporated Image Pulverizer.  Please insert tip.\n")
SingleOrMulti = input("type f for a whoole folder(SortAll), else you get one pic.\n")
if SingleOrMulti == "f":
    #directory = os.getenv("folder_input_path")
    directory = "C:\\Users\\mwk\\Desktop\\thrushArt\\PICTURESToSORT\\Unsorted\\SortAll\\"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            input_path = f
            output_path = os.getenv("output_path")
            print(f)
            foldersorter(f, output_path)
else:
    #runs userinput script, then pixelsorter script
    input_path, output_path = userInput()
    pixelsorter(input_path, output_path)