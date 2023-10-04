import os

sound_files = os.listdir('sounds')

for file_name in sound_files:
    old_name = file_name

    if (file_name[0] == '.'):   # remove . from start of file name
        file_name = file_name[1:]
    
    file_name_split = file_name.split(".")
    if (file_name_split[len(file_name_split)-1] == "icloud"):   # remove .icloud from file name
        file_name_split = file_name_split[:-1]
    
    new_name = '.'.join(file_name_split)   # sanitized file name

    os.rename("sounds/"+ old_name, "sounds/"+new_name)