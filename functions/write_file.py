import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if abs_file_path.startswith(abs_working_directory + os.sep):
        try:
            dir_path = os.path.dirname(abs_file_path)
            if os.path.exists(dir_path):
                with open(abs_file_path, "w") as f:
                    f.write(content)
            else:
                os.makedirs(dir_path)
                with open(abs_file_path, "w") as f:
                    f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
        except Exception as e:
            return f"Error: {str(e)}"


    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    