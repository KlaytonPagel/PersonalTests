# Program used to add a file extension to files
import os

folder = os.listdir("files")

for file in folder:
    os.rename("files/" + file, "files/" + file + ".wav")
print("Finished")
