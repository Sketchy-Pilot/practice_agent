from argparse import ArgumentDefaultsHelpFormatter
import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a file in a specified file_path relative to the working directory. It outputs STDOUT, STDERR, and the exit code the process exited with if there was an error.",
        "parameters":{
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file path to run, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "a list of optional arguments for the python file."
                },
            },
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        output = ""
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir is False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_dir) is False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if target_dir.endswith(".py") is False:
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_dir]
        if args is not None:
            command.extend(args)
        ai_run = subprocess.run(command, capture_output=True,text=True,timeout=30)
        if ai_run.returncode != 0:
            output += f"Process exited with code {ai_run.returncode}\n"
        if ai_run.stderr == "" and ai_run.stdout == "":
            output += "No output produced"
        else:
            output += f"STDOUT: {ai_run.stdout}\nSTDERR: {ai_run.stderr}"
        return output

    except Exception as e:
        return f'Error: {e}'
