import os

def list_directory_contents(path='my folder'):
    """
    Lists files and directories in the given path (default is current directory).
    """
    try:
        entries = os.listdir(path)  # Returns a list of names (files and directories) :contentReference[oaicite:0]{index=0}
        for name in entries:
            print(name)
    except FileNotFoundError:
        print(f'Error: The directory "{path}" does not exist.')
    except PermissionError:
        print(f'Error: Permission denied for directory "{path}".')

if __name__ == "__main__":
    # You can change this to any directory you'd like to inspect
    dir_to_list = input("Enter directory path (press Enter for current directory): ") or '.'
    list_directory_contents(dir_to_list)
