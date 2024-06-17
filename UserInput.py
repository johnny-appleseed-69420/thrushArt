
from dotenv import load_dotenv
import os

#load environment variables
load_dotenv()

#get user input
def userInput():
    #get user input for file path information
    initialName = input("What is the name of the image you want to fuck up? (Case-Sensitive)\n")
    fileType = input("What is the file type of the image you want to fuck up? If you already input a file type, just hit enter.\n")
    finalName = input("What do you want to call the fucked up image?\n")

    #determine what file will be sorted, and what it should be called.  Uses .env to get paths.
    input_path = os.getenv("input_path") + initialName + fileType
    output_path = os.getenv("output_path") + finalName + ".png"

    return input_path, output_path