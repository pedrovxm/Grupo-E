import os

def get_all_files(dir_name):
    folder_content = os.listdir(dir_name)
    all_files = list()
    for entry in folder_content:
        entry_path = os.path.join(dir_name, entry)
        if os.path.isdir(entry_path):
            all_files = all_files + get_all_files(entry_path)
        else:
            all_files.append(entry_path)                
    return all_files