import os
import shutil


class Copier:

    # Set up the destination and get the files in the source folder_____________________________________________________
    def __init__(self):
        self.destination_path = '../../klaytonpagel.github.io'
        self.source_folder = os.listdir("../../html-practice")
        self.source_path_base = "../../html-practice/"
        self.source_list = []

        self.make_list()
        self.run()

    # Construct a list of files to copy excluding ones I don't want to copy_____________________________________________
    def make_list(self):
        excluded_files = [".git", ".idea", "role-playing-game", "calorie counter", "canvas_testing"]
        for file in self.source_folder:
            if file in excluded_files:
                self.source_list.append(file)

    # Copy the source file to the destination folder____________________________________________________________________
    def copy_file(self, source_path):
        shutil.copy2(source_path, self.destination_path)

    # For each file in the source list turn it into the source path then copy it________________________________________
    def run(self):
        for file in self.source_list:
            source_path = self.source_path_base + file
            self.copy_file(source_path)

Copier()
