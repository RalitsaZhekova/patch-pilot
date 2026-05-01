import os

MAX_CHARS = 10_000

def get_file_content(working_dir, file_path):
    working_dir_abs = os.path.abspath(working_dir)
    target_file_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))

    valid_target_file = os.path.commonpath([working_dir_abs, target_file_abs]) == working_dir_abs
    if not valid_target_file:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        content = ""
        with open(target_file_abs, "r") as file:
            file_content = file.read(MAX_CHARS)
            content += file_content
            if file.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content
    except Exception as e:
        return f'Error: {e}'