import os
level_folder = 'Angaben/level-1'

def find_level(level_folder):
    input_files = []
    content = os.listdir(level_folder)
    for c in content:
        if 'in_level' in c.split('-')[0]:
            input_files.append(c)
        else:
            continue
    return input_files


#print(find_level(level_folder))