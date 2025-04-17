import tkinter as tk
from tkinter import filedialog

def get_folder():
    global folder
    try:
        root = tk.Tk()
        root.withdraw()
        folder = filedialog.askdirectory(title="Select the root folder for the server!")

        if not folder:
            raise ValueError("No Folder Selected!")

        return folder

    except Exception as e:
        print(f"Error: {e}")
