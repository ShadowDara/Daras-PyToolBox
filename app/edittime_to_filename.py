import os
import re
from datetime import datetime

def main(folder):
    date_prefix_pattern = re.compile(r"^\d{4}\.\d{2}\.\d{2} ")

    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)

        if not os.path.isfile(full_path):
            continue

        if date_prefix_pattern.match(filename):
            print(f"Skipped (with date): {filename}")
            continue

        last_modified = datetime.fromtimestamp(os.path.getmtime(full_path))
        date_prefix = last_modified.strftime("%Y.%m.%d")

        new_filename = f"{date_prefix} {filename}"
        new_full_path = os.path.join(folder, new_filename)

        if os.path.exists(new_full_path):
            print(f"File is existing: {new_filename} - skipping")
            continue

        os.rename(full_path, new_full_path)
        print(f"Renamed: {filename} -> {new_filename}")
