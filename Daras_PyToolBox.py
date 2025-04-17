# Python Toolbox by Shadowdara

import os
import sys

# import scripts
import app.convert_3ma_to_obj
import app.delete_step_by_step
import app.info
import app.select_folder
import app.settings
import app.shadow_path_2_0
import app.simple_http_server
import app.styles

# main function
def main():
    path = os.path.dirname(os.path.abspath(__file__))
    while True:
        choice = input("Type info for more Infos: ---> ").lower()

        if choice == '0' or choice == 'exit 0':
            sys.exit(0)
        elif choice == 'info':
            app.info.main()

        # to check if the config file is available
        elif choice == '1':
            if app.settings.check_file(path):
                pass

# run on execution
if __name__ == '__main__':
    print("PyToolBox by Shadowdara\n")

    main()
