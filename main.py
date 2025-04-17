# Python Toolbox by Shadowdara

import os
import sys

# import scripts
import app.convert_3ma_to_obj

import app.delete_step_by_step

import app.select_folder

# main function
def main():
    while True:
        choice = input("Type info for more Infos: ---> ").lower()

        if choice == '0' or choice == 'exit 0':
            sys.exit(1)

# run on execution
if __name__ == '__main__':
    print("PyToolBox by Shadowdara\n")

    main()
