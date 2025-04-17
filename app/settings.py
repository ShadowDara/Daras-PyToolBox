import os
import configparser

def check_file(path):
    try:
        with open(os.path.join(path, 'settings', 'config.ini'), "rt", encoding='UTF-8'):
            return True
    except FileNotFoundError as e:
        print(f'Error: {e}')

def read_settings():
    pass

def create_settings():
    pass
