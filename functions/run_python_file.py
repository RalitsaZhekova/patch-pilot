import os
import subprocess

def run_python_file(working_dir, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_dir)
        target_file_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file_abs]) == working_dir_abs
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file_abs]
        if args is None:
            args = []
        command.extend(args)

        completed_process = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output = []
        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")

        if not completed_process.stdout and not completed_process.stderr:
            output.append("No output produced")
        else:
            if completed_process.stdout:
                output.append(f"STDOUT:\n{completed_process.stdout}")
            if completed_process.stderr:
                output.append(f"STDERR:\n{completed_process.stderr}")

        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
