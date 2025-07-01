import os

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory)
    abs_working_directory = os.path.abspath(working_directory)
    abs_target_path = os.path.abspath(full_path)

    if abs_target_path.startswith(abs_working_directory):
        if os.path.isdir(abs_target_path):
            try:
                listed = os.listdir(abs_target_path)
                contents = []
                for item in listed:
                    item_path = os.path.join(abs_target_path, item)
                    is_dir = os.path.isdir(item_path)
                    size = os.path.getsize(item_path)
                    contents.append(f'- {item}: file_size={size} bytes, is_dir={is_dir}')
                return '\n'.join(contents)
            except Exception as e:
                return f'Error: {str(e)}'
        else:
            return f'Error: "{directory}" is not a directory'
    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
