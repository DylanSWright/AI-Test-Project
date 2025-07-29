import os

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_working_directory = os.path.abspath(working_directory)
    abs_target_path = os.path.abspath(full_path)

    if abs_target_path.startswith(abs_working_directory):
        if os.path.isfile(abs_target_path):
            MAX_CHARS = 10000
            try:
                with open(abs_target_path, "r") as f:
                    file_content_string = f.read(MAX_CHARS)
                    if len(file_content_string) >= MAX_CHARS:
                        return f'{file_content_string}[...File "{file_path}" truncated at 10000 characters]'
                    else:
                        return f'{file_content_string}'
            except Exception as e:
                return f'Error: {str(e)}'
        else:
            return f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'