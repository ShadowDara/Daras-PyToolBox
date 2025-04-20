import os
import subprocess

def main(base_path):
    ghd_path = os.path.expandvars(r"%LOCALAPPDATA%\GitHubDesktop\GitHubDesktop.exe")
    if not os.path.exists(ghd_path):
        print(f"Github Desktop not found: {ghd_path}")


    for name in os.listdir(base_path):
        full_path = os.path.join(base_path, name)
        git_path = os.path.join(full_path, ".git")
    
        if os.path.isdir(full_path) and os.path.isdir(git_path):
            print(f"Opening Repository: {name}")
            subprocess.Popen([ghd_path, full_path])
