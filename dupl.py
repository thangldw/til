import os

def find_and_delete_files():
    target_file_format = ""
    target_file_with_capacity_format = " 2."

    for root, dirs, files in os.walk('.'):  # Replace '.' with the directory path you want to search in
        for file_name in files:
            if target_file_with_capacity_format in file_name:
                capacity_file_path = os.path.join(root, file_name)
                capacity = os.path.getsize(capacity_file_path)
                print(file_name, capacity)

                # Check if any file matches the target format "XXX"
                for target_file_name in files:
                    if target_file_format in target_file_name:
                        target_file_path = os.path.join(root, target_file_name)
                        if os.path.isfile(target_file_path):
                            target_file_capacity = os.path.getsize(target_file_path)
                            print(target_file_format)

                            # Compare capacities
                            if capacity == target_file_capacity:
                                os.remove(capacity_file_path)
                                print(f"Deleted file: {capacity_file_path}")
                                break

                        else:
                            print(f"File with format '{target_file_format}' not found.")

find_and_delete_files()