import os
import config

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads a file in the specified file_path relative to the working directory. It will read the file up to a specified limit, then truncate with a message notifying that it was truncated",
        "parameters":{
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file path to read, relative to the working directory (default is the working directory itself)",
                },
            }
        }
    }
}

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir is False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_dir) is False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_dir, "r") as f:
            content = f.read(config.MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f'Error: {e}'
