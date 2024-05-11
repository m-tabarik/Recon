import os

def process_file(file_name):
    # Replace this line with the command you want to execute for each file
    command = f"nuclei -l {file_name} -t ../tomcat-detect.yaml "
    os.system(command)
  
def traverse_folder(folder_path):
    # List all files in the specified folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
  
    # Process each file
    for file_name in files: 
        process_file(file_name)

if __name__ == "__main__":
    # Get the current working directory as the folder path
    folder_path = os.getcwd()

    # Traverse the folder and process each file
    traverse_folder(folder_path)
