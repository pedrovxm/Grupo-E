import os

def count_files(dir_name):
    folder_content = os.listdir(dir_name)
    count = 0
    for entry in folder_content:
        entry_path = os.path.join(dir_name, entry)
        if os.path.isdir(entry_path):
            count += count_files(entry_path)
        else:
            count += 1                
    return count