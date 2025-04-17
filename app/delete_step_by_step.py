import os

def delete_step_by_step(folder):
    while True:
        next_file = None
        for entry in os.scandir(folder):
            if entry.is_file():
                next_file = entry.path
                break

        if not next_file:
            print("No more files found.")
            break

        file_name = os.path.basename(next_file)

        try:
            os.remove(next_file)
            print(f"Deleted: {file_name}")
        except Exception as e:
            print(f"Error deleting {file_name}: {e}")

    print("Done.")
