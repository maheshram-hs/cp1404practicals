"""
Program to sort and organise files based on filetype.

Sort Files 1. Created by Maheshram Shunmuganand, February 2022
"""

import os
import shutil


def main():
    """Creat directories for each filetype and sort all files appropriately."""
    os.chdir("FilesToSort")
    for directory_name, subdirectories, filenames in os.walk('.'):

        # Make list of all the types of extensions.
        # Make a dictionary of filename and extension type pair.
        extensions = []
        filename_to_extension = {}
        for filename in filenames:
            ext = filename.split('.')
            extensions.append(ext[-1])
            filename_to_extension[filename] = ext[-1]

        # Make a list of all the unique and different types of extensions.
        extension_types = []
        for extension in extensions:
            if extension not in extension_types:
                extension_types.append(extension)

        # Create directories for each file type.

        for ext_type in extension_types:
            dir_name = input(f"What category would you like to sort {ext_type} files into? ")
            try:
                os.mkdir(dir_name)
            except FileExistsError:
                continue

            # Move all files to its own appropriate directories.
            for key, value in filename_to_extension.items():
                if value == ext_type:
                    shutil.move(key, f'{dir_name}/')


if __name__ == '__main__':
    main()
