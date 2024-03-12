import os
import shutil

destination_path = '../../klaytonpagel.github.io'
source_folder = os.listdir("../../html-practice")

print(source_folder)


def make_list():
    excluded_files = [".git", ".idea", "role-playing-game", "calorie counter", "canvas_testing"]
    for file in source_folder:
        if file in excluded_files:
            print(file)


def copy_file(source_path):
    shutil.copy2(source_path, destination_path)


make_list()


# shutil.copy2(source_path, destination_path)
