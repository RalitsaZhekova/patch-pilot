import os

def get_files_info(working_dir, dir=".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_dir)
        target_dir = os.path.abspath(os.path.join(working_dir_abs, dir))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{dir}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{dir}" is not a directory'

        contents = []
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            contents.append(
                f"- {item}: file_size={os.path.getsize(item_path)} bytes, "
                f"is_dir={os.path.isdir(item_path)}"
            )

        return "\n".join(contents)
    except Exception as e:
        return f"Error: {e}"
