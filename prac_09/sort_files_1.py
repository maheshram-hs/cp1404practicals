"""
...

Sort Files 1. Created by Maheshram Shunmuganand, February 2022
"""

import os
import shutil


def main():
    """..."""
    os.chdir("FilesToSort")
    for directory_name, subdirectories, filenames in os.walk('.'):

        extensions = []
        filename_to_extension = {}
        for filename in filenames:
            ext = filename.split('.')
            extensions.append(ext[-1])
            filename_to_extension[filename] = ext[-1]

        extension_types = []
        for extension in extensions:
            if extension not in extension_types:
                extension_types.append(extension)

        print(extension_types)
        print(filename_to_extension)
        print(filenames)

        for ext_type in extension_types:
            try:
                os.mkdir(ext_type)
            except FileExistsError:
                continue


if __name__ == '__main__':
    main()
