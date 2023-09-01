import os
import shutil

def search_files_in_folder(folder_path, keywords):
    matching_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if all(keyword in file for keyword in keywords):
                matching_files.append(os.path.join(root, file))
    return matching_files

def display_matching_files(matching_files):
    for i, file in enumerate(matching_files, 1):
        print(f"{i}. {file}")

def main():
    folder_path = input("Enter the path of the folder to search in: ")
    keywords = input("Enter keywords (comma-separated) to search for: ").split(",")
    keywords = [keyword.strip() for keyword in keywords]

    matching_files = search_files_in_folder(folder_path, keywords)

    if not matching_files:
        print("No matching files found.")
        return

    print("Matching files:")
    display_matching_files(matching_files)

    try:
        selected_index = int(input("Enter the number of the file to Copy (e.g., 1, 2, etc.): ")) - 1
        if selected_index < 0 or selected_index >= len(matching_files):
            print("Invalid choice.")
            return

        selected_file = matching_files[selected_index]

        destination_path = input("Enter the destination path to copy the selected file: ")
        shutil.copy(selected_file, destination_path)
        print(f"File '{selected_file}' copied to '{destination_path}' successfully.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
