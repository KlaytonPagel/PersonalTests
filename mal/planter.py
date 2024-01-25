import os
import shutil


source_path = os.getcwd()
source_path = source_path + '\\BigA.exe'
os.chdir('C:/Users')


def find_startup():
    for root, dir, file in os.walk('C:'):
        if 'Startup' in dir:
            print('\n \n found')
            return 'C:\\Users\\' + root.split('C:')[1] + '\\Startup'
        print(root, dir, file)


destination_path = find_startup()

shutil.copy2(source_path, destination_path)

print('complete')
