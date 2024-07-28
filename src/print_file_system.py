import os
import json

def read_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

def print_file_system(folder_path, exclude_files, excluded_folders, indent=""):
    file_structure = ""
    with os.scandir(folder_path) as entries:
        for entry in entries:
            if entry.name in excluded_folders:
                continue
            if entry.is_dir():
                file_structure += f"{indent}{entry.name}/\n"
                file_structure += print_file_system(os.path.join(folder_path, entry.name), exclude_files, excluded_folders, indent + "    ")
            elif not exclude_files:
                file_structure += f"{indent}{entry.name}\n"
    return file_structure

def main():
    config = read_config('C:/atari-monk/code/piano/data/print_file_system_config.json')
    folder_path = config.get('folder_path')
    output_file = config.get('output_file')
    exclude_files = config.get('exclude_files', False)
    excluded_folders = config.get('excluded_folders', [])

    if not folder_path or not output_file:
        print("Please make sure 'folder_path' and 'output_file' are set in the config file.")
        return

    file_structure = print_file_system(folder_path, exclude_files, excluded_folders)

    with open(output_file, 'w') as file:
        file.write(file_structure)

    print(f"File structure has been written to {output_file}")

if __name__ == "__main__":
    main()
