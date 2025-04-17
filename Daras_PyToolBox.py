# Python Toolbox by Shadowdara

import os, sys

# import scripts here
from app import select_folder, delete_step_by_step, convert_3ma_to_obj, simple_http_server, info, shadow_path_2_0, styles
from test import list

# main function
def main():
    path = os.path.dirname(os.path.abspath(__file__))
    while True:
        choice = input("Type info for more Infos: ---> ").lower()
        print("""
Command List:

0   return 
1   to delete all files in a selected Folder
2   to convert 3ma to obj files
3   to start a simple HTTP Server
""")
        choice = input("Select: ")
        if choice == '1':
            folder = select_folder.get_folder()
            delete_step_by_step.delete_step_by_step(folder)
        elif choice == '2':
            folder = select_folder.get_folder()
            convert_3ma_to_obj.find_files(folder)
        elif choice == '3':
            simple_http_server.main(folder)
        elif choice == '0' or choice == 'exit 0':
            sys.exit(0)
        elif choice == 'info':
            info.main()
        elif choice == 'license':
            info.license()
        elif choice == 'game':
            shadow_path_2_0.start_game()
        elif choice =='c':
            list.main()

# run on execution
if __name__ == '__main__':
    styles.p_magenta("PyToolBox by Shadowdara\n")
    main()
