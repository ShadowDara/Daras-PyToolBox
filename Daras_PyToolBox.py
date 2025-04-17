# Python Toolbox by Shadowdara

import os, sys

# import scripts here
import app.select_folder, app.delete_step_by_step, app.convert_3ma_to_obj, app.simple_http_server, app.info, app.shadow_path_2_0, app.styles, app.edittime_to_filename

# main function
def main():
    path = os.path.dirname(os.path.abspath(__file__))
    while True:
        print("Type info for more Infos")
        print("""
Command List:

0   return 
1   to delete all files in a selected Folder
2   to convert 3ma to obj files
3   to start a simple HTTP Server
4   to add the file edittime to the filename
""")
        choice = input("Select: ").lower()
        if choice == '1':
            folder = app.select_folder.get_folder()
            app.delete_step_by_step.delete_step_by_step(folder)
        elif choice == '2':
            folder = app.select_folder.get_folder()
            app.convert_3ma_to_obj.find_files(folder)
        elif choice == '3':
            folder = app.select_folder.get_folder()
            app.simple_http_server.main(folder)
        elif choice == '4':
            folder = app.select_folder.get_folder()
            app.edittime_to_filename.main(folder)
        elif choice == '0' or choice == 'exit 0':
            sys.exit(0)
        elif choice == 'info':
            app.info.main()
        elif choice == 'license':
            app.info.license()
        elif choice == 'game':
            app.shadow_path_2_0.start_game()

# run on execution
if __name__ == '__main__':
    app.styles.p_magenta("PyToolBox by Shadowdara\n")
    main()
